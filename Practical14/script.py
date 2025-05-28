import xml.dom.minidom
import xml.sax
import datetime
from collections import defaultdict
import os

# Get the directory of the current script
current_dir = os.path.dirname(os.path.abspath(__file__))

# DOM parsing implementation
def parse_dom(xml_file):
    try:
        start_time = datetime.datetime.now()
        doc = xml.dom.minidom.parse(xml_file)
        terms = doc.getElementsByTagName("term")
        
        term_data = {}
        for term in terms:
            try:
                id_node = term.getElementsByTagName("id")[0].firstChild
                namespace_node = term.getElementsByTagName("namespace")[0].firstChild
                if id_node and namespace_node:
                    term_id = id_node.nodeValue
                    namespace = namespace_node.nodeValue
                    is_a_list = term.getElementsByTagName("is_a")
                    term_data[term_id] = {
                        'namespace': namespace, 
                        'is_a_count': len(is_a_list)
                    }
            except (IndexError, AttributeError) as e:
                continue  # Skip malformed term entries
        
        # Find the term with the highest <is_a> count for each namespace
        max_terms = {
            'molecular_function': (None, 0), 
            'biological_process': (None, 0), 
            'cellular_component': (None, 0)
        }
        
        for term_id, data in term_data.items():
            namespace = data['namespace']
            if namespace in max_terms:
                current_max_id, current_max_count = max_terms[namespace]
                if data['is_a_count'] > current_max_count:
                    max_terms[namespace] = (term_id, data['is_a_count'])
        
        end_time = datetime.datetime.now()
        time_taken = (end_time - start_time).total_seconds()
        
        return {
            'molecular_function': max_terms['molecular_function'],
            'biological_process': max_terms['biological_process'],
            'cellular_component': max_terms['cellular_component'],
            'time_taken': time_taken
        }
    
    except Exception as e:
        print(f"DOM Parsing Error: {str(e)}")
        return None

# SAX parsing implementation
class GoTermHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.current_term = False
        self.current_tag = ''
        self.current_id = ''
        self.current_namespace = ''
        self.is_a_count = 0
        self.term_data = defaultdict(lambda: {'namespace': '', 'is_a_count': 0})
        self.chars_buffer = []
    
    def startElement(self, tag, attrs):
        self.current_tag = tag
        if tag == 'term':
            self.current_term = True
            self.is_a_count = 0
            self.current_id = ''
            self.current_namespace = ''
        elif tag == 'is_a' and self.current_term:
            self.is_a_count += 1
        self.chars_buffer = []
    
    def endElement(self, tag):
        content = ''.join(self.chars_buffer).strip()
        if tag == 'term' and self.current_term:
            if self.current_id:
                self.term_data[self.current_id] = {
                    'namespace': self.current_namespace,
                    'is_a_count': self.is_a_count
                }
            self.current_term = False
        elif tag == 'id' and self.current_term:
            self.current_id = content
        elif tag == 'namespace' and self.current_term:
            self.current_namespace = content
        self.chars_buffer = []
    
    def characters(self, content):
        if self.current_term:
            self.chars_buffer.append(content)

def parse_sax(xml_file):
    try:
        start_time = datetime.datetime.now()
        parser = xml.sax.make_parser()
        parser.setFeature(xml.sax.handler.feature_namespaces, 0)
        handler = GoTermHandler()
        parser.setContentHandler(handler)
        parser.parse(xml_file)
        
        # Find the term with the highest <is_a> count for each namespace
        max_terms = {
            'molecular_function': (None, 0), 
            'biological_process': (None, 0), 
            'cellular_component': (None, 0)
        }
        
        for term_id, data in handler.term_data.items():
            namespace = data['namespace']
            if namespace in max_terms:
                current_max_id, current_max_count = max_terms[namespace]
                if data['is_a_count'] > current_max_count:
                    max_terms[namespace] = (term_id, data['is_a_count'])
        
        end_time = datetime.datetime.now()
        time_taken = (end_time - start_time).total_seconds()
        
        return {
            'molecular_function': max_terms['molecular_function'],
            'biological_process': max_terms['biological_process'],
            'cellular_component': max_terms['cellular_component'],
            'time_taken': time_taken
        }
    
    except Exception as e:
        print(f"SAX Parsing Error: {str(e)}")
        return None

# Main function
def main():
    xml_file = os.path.join(current_dir, "go_obo.xml")  # Path to the XML file
    
    if not os.path.exists(xml_file):
        print(f"Error: XML file not found at {xml_file}")
        return
    
    print("DOM Parsing Results:")
    dom_results = parse_dom(xml_file)
    if dom_results:
        print(f"Molecular Function: ID={dom_results['molecular_function'][0] or 'N/A'}, <is_a> count={dom_results['molecular_function'][1]}")
        print(f"Biological Process: ID={dom_results['biological_process'][0] or 'N/A'}, <is_a> count={dom_results['biological_process'][1]}")
        print(f"Cellular Component: ID={dom_results['cellular_component'][0] or 'N/A'}, <is_a> count={dom_results['cellular_component'][1]}")
        print(f"DOM Parsing Time: {dom_results['time_taken']:.4f} seconds\n")
    
    print("SAX Parsing Results:")
    sax_results = parse_sax(xml_file)
    if sax_results:
        print(f"Molecular Function: ID={sax_results['molecular_function'][0] or 'N/A'}, <is_a> count={sax_results['molecular_function'][1]}")
        print(f"Biological Process: ID={sax_results['biological_process'][0] or 'N/A'}, <is_a> count={sax_results['biological_process'][1]}")
        print(f"Cellular Component: ID={sax_results['cellular_component'][0] or 'N/A'}, <is_a> count={sax_results['cellular_component'][1]}")
        print(f"SAX Parsing Time: {sax_results['time_taken']:.4f} seconds\n")
    
    # Compare the performance of the two methods
    if dom_results and sax_results:
        if dom_results['time_taken'] < sax_results['time_taken']:
            print("DOM was faster in this run")
            # DOM is generally slower for large files, but might be faster for small ones
        else:
            print("SAX was faster in this run")
            # SAX is generally faster for large XML files like go_obo.xml

if __name__ == "__main__":
    main()