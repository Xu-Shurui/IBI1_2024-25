import xml.dom.minidom
import xml.sax
import time
import datetime
from collections import defaultdict
import os

# Get the directory of the current script
current_dir = os.path.dirname(os.path.abspath(__file__))

# DOM parsing implementation
def parse_dom(xml_file):
    start_time = datetime.datetime.now()
    doc = xml.dom.minidom.parse(xml_file)
    terms = doc.getElementsByTagName("term")
    
    term_data = {}
    for term in terms:
        id = term.getElementsByTagName("id")[0].firstChild.nodeValue
        namespace = term.getElementsByTagName("namespace")[0].firstChild.nodeValue
        is_a_list = term.getElementsByTagName("is_a")
        term_data[id] = {'namespace': namespace, 'is_a_count': len(is_a_list)}
    
    # Find the term with the highest <is_a> count for each namespace
    max_terms = {'molecular_function': ('', 0), 'biological_process': ('', 0), 'cellular_component': ('', 0)}
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

# SAX parsing implementation
class GoTermHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.current_term = None
        self.current_tag = ''
        self.current_id = ''
        self.current_namespace = ''
        self.is_a_count = 0
        self.term_data = defaultdict(lambda: {'namespace': '', 'is_a_count': 0})
    
    def startElement(self, tag, attrs):
        self.current_tag = tag
        if tag == 'term':
            self.current_term = True
            self.is_a_count = 0
        elif tag == 'is_a':
            self.is_a_count += 1
    
    def endElement(self, tag):
        if tag == 'term':
            self.term_data[self.current_id] = {
                'namespace': self.current_namespace,
                'is_a_count': self.is_a_count
            }
            self.current_term = False
    
    def characters(self, content):
        if self.current_tag == 'id' and self.current_term:
            self.current_id = content
        elif self.current_tag == 'namespace' and self.current_term:
            self.current_namespace = content

def parse_sax(xml_file):
    start_time = datetime.datetime.now()
    parser = xml.sax.make_parser()
    handler = GoTermHandler()
    parser.setContentHandler(handler)
    parser.parse(xml_file)
    
    # Find the term with the highest <is_a> count for each namespace
    max_terms = {'molecular_function': ('', 0), 'biological_process': ('', 0), 'cellular_component': ('', 0)}
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

# Main function
def main():
    xml_file = os.path.join(current_dir, "go_obo.xml")  # Path to the XML file
    
    print("DOM Parsing Results:")
    dom_results = parse_dom(xml_file)
    print(f"Molecular Function: ID={dom_results['molecular_function'][0]}, <is_a> count={dom_results['molecular_function'][1]}")
    print(f"Biological Process: ID={dom_results['biological_process'][0]}, <is_a> count={dom_results['biological_process'][1]}")
    print(f"Cellular Component: ID={dom_results['cellular_component'][0]}, <is_a> count={dom_results['cellular_component'][1]}")
    print(f"DOM Parsing Time: {dom_results['time_taken']} seconds\n")
    
    print("SAX Parsing Results:")
    sax_results = parse_sax(xml_file)
    print(f"Molecular Function: ID={sax_results['molecular_function'][0]}, <is_a> count={sax_results['molecular_function'][1]}")
    print(f"Biological Process: ID={sax_results['biological_process'][0]}, <is_a> count={sax_results['biological_process'][1]}")
    print(f"Cellular Component: ID={sax_results['cellular_component'][0]}, <is_a> count={sax_results['cellular_component'][1]}")
    print(f"SAX Parsing Time: {sax_results['time_taken']} seconds\n")
    
    # Compare the performance of the two methods
    if dom_results['time_taken'] < sax_results['time_taken']:
        print("DOM is faster")
    else:
        print("SAX is faster")

if __name__ == "__main__":
    main()