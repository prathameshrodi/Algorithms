"""
__author__ = "Prathamesh Rodi"
__copyright__ = "Copyright 2022"
__project__ = "Algorithms"
__version__ = "0.0.1"
__maintainer__ = "Prathamesh Rodi"
__email__ = "prathameshrodi3009@gmail.com"
"""


class Transcript:
    index = 0
    stack = list()

    def main(self, html):
        result = list()
        code = html.split('\n')
        for each_element in code:
            each_element = each_element.strip()
            if not each_element:
                continue
            if each_element.startswith("tag:"):
                tag = f"<{each_element.strip('tag:')}>"
                self.stack.append(f"<\{each_element.strip('tag:')}>")
            else:
                tag = each_element
            result.append(f"{tag}")
        result.extend([self.stack.pop(-1) for ele in range(len(self.stack))])
        return ''.join(result)


if __name__ == '__main__':
    t = Transcript()
    print(t.main('''tag:html
    tag:div
        Leet
        tag:span
            code
		tag:span
			.com'''))
