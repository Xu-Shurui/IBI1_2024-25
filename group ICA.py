import pandas as pd
import matplotlib.pyplot as plt
from typing import Optional, Dict

class AminoAcidAnalyzer:
    """
    氨基酸频率分析工具类
    
    功能：
    - 自动将 mRNA 序列翻译为氨基酸序列
    - 统计氨基酸频率
    - 生成可视化图表
    
    使用示例：
    >>> analyzer = AminoAcidAnalyzer()
    >>> analyzer.analyze_and_plot("AUGUUUCUACUAG")  # 快捷分析
    >>> # 分步使用
    >>> aa_seq = analyzer.translate_sequence("AUGUUU")
    >>> freq = analyzer.calculate_frequency(aa_seq)
    >>> analyzer.plot_frequency(freq, title="Custom Title")
    """
    
    # 类级别常量：密码子表（内存中只保存一份）
    CODON_TABLE = pd.DataFrame({
        'Codon': [
            'UUU', 'UUC', 'UUA', 'UUG', 'CUU', 'CUC', 'CUA', 'CUG',
            'AUU', 'AUC', 'AUA', 'AUG', 'GUU', 'GUC', 'GUA', 'GUG',
            'UCU', 'UCC', 'UCA', 'UCG', 'CCU', 'CCC', 'CCA', 'CCG',
            'ACU', 'ACC', 'ACA', 'ACG', 'GCU', 'GCC', 'GCA', 'GCG',
            'UAU', 'UAC', 'UAA', 'UAG', 'CAU', 'CAC', 'CAA', 'CAG',
            'AAU', 'AAC', 'AAA', 'AAG', 'GAU', 'GAC', 'GAA', 'GAG',
            'UGU', 'UGC', 'UGA', 'UGG', 'CGU', 'CGC', 'CGA', 'CGG',
            'AGU', 'AGC', 'AGA', 'AGG', 'GGU', 'GGC', 'GGA', 'GGG'
        ],
        'AminoAcid': [
            'F', 'F', 'L', 'L', 'L', 'L', 'L', 'L',
            'I', 'I', 'I', 'M', 'V', 'V', 'V', 'V',
            'S', 'S', 'S', 'S', 'P', 'P', 'P', 'P',
            'T', 'T', 'T', 'T', 'A', 'A', 'A', 'A',
            'Y', 'Y', '*', '*', 'H', 'H', 'Q', 'Q',
            'N', 'N', 'K', 'K', 'D', 'D', 'E', 'E',
            'C', 'C', '*', 'W', 'R', 'R', 'R', 'R',
            'S', 'S', 'R', 'R', 'G', 'G', 'G', 'G'
        ]
    }).set_index('Codon')['AminoAcid']

    def __init__(self, plot_config: Optional[Dict] = None):
        """
        初始化分析器
        
        :param plot_config: 绘图配置字典，可选参数：
            - figsize: 图表尺寸 (默认 (12,6))
            - color_map: 颜色映射名称 (默认 'tab20')
            - title: 标题 (默认 'Amino Acid Frequency Distribution')
            - edgecolor: 条形边框颜色 (默认 'black')
            - fontsize: 基础字号 (默认 12)
        """
        self.plot_config = plot_config or {}
        self._default_config = {
            'figsize': (12, 6),
            'color_map': 'tab20',
            'title': 'Amino Acid Frequency Distribution',
            'edgecolor': 'black',
            'fontsize': 12
        }

    def translate_sequence(self, mrna: str) -> pd.Series:
        """
        翻译 mRNA 序列为氨基酸序列
        
        :param mrna: 输入 mRNA 序列（不区分大小写）
        :return: 包含氨基酸序列的 pandas Series
        """
        # 输入验证
        if not isinstance(mrna, str) or len(mrna) < 3:
            raise ValueError("Invalid mRNA sequence: must be a string with at least 3 bases")
        
        # 预处理
        mrna_upper = mrna.upper()
        valid_bases = {'A', 'U', 'G', 'C'}
        if not set(mrna_upper) <= valid_bases:
            invalid = set(mrna_upper) - valid_bases
            raise ValueError(f"Invalid bases detected: {invalid}")

        # 分割密码子
        codons = [mrna_upper[i:i+3] for i in range(0, len(mrna_upper)-2, 3)]
        
        # 翻译序列
        aa_series = pd.Series(codons).map(self.CODON_TABLE)
        
        # 处理终止密码子
        if '*' in aa_series.values:
            stop_idx = aa_series[aa_series == '*'].index[0]
            aa_series = aa_series.iloc[:stop_idx]
        
        return aa_series

    def calculate_frequency(self, aa_series: pd.Series) -> pd.Series:
        """
        计算氨基酸频率
        
        :param aa_series: translate_sequence() 输出的氨基酸序列
        :return: 按频率降序排列的 Series
        """
        return aa_series.value_counts().sort_values(ascending=False)

    def plot_frequency(self, freq_series: pd.Series, **kwargs) -> plt.Axes:
        """
        绘制频率分布图
        
        :param freq_series: calculate_frequency() 输出的频率数据
        :param kwargs: 可覆盖 self.plot_config 的参数
        :return: matplotlib Axes 对象
        """
        # 合并配置参数
        config = {**self._default_config, **self.plot_config, **kwargs}
        
        # 创建画布
        plt.figure(figsize=config['figsize'])
        ax = freq_series.plot.bar(
            color=plt.get_cmap(config['color_map']).colors,
            edgecolor=config['edgecolor']
        )
        
        # 添加标签
        for p in ax.patches:
            ax.annotate(
                f"{p.get_height()}",
                (p.get_x() + p.get_width()/2, p.get_height()),
                ha='center', va='bottom',
                fontsize=config['fontsize']-2
            )
        
        # 设置样式
        ax.set_title(config['title'], fontsize=config['fontsize']+2, pad=20)
        ax.set_xlabel('Amino Acid', fontsize=config['fontsize'], labelpad=10)
        ax.set_ylabel('Count', fontsize=config['fontsize'], labelpad=10)
        ax.grid(axis='y', linestyle='--', alpha=0.7)
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        
        return ax

    def analyze_and_plot(self, mrna: str) -> Optional[plt.Axes]:
        """
        一站式分析流程
        
        :param mrna: 输入 mRNA 序列
        :return: 若成功返回 Axes 对象，否则返回 None
        """
        try:
            aa_series = self.translate_sequence(mrna)
            if aa_series.empty:
                print("No amino acids to plot.")
                return None
                
            freq = self.calculate_frequency(aa_series)
            return self.plot_frequency(freq)
        except Exception as e:
            print(f"Analysis failed: {str(e)}")
            return None
