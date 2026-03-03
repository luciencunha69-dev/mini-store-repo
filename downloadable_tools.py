# downloadable_tools.py

from dataclasses import dataclass
from typing import List, Optional

@dataclass
class Tool:
    name: str
    version: str
    url: str

class DownloadableToolsList:
    def __init__(self):
        self.tools: List[Tool] = []

    def add_tool(self, tool: Tool):
        self.tools.append(tool)

    def remove_tool(self, tool_name: str):
        self.tools = [tool for tool in self.tools if tool.name != tool_name]

    def filter_tools(self, version: Optional[str] = None) -> List[Tool]:
        if version:
            return [tool for tool in self.tools if tool.version == version]
        return self.tools

# Example usage
if __name__ == '__main__':
    tools_list = DownloadableToolsList()
    tool1 = Tool(name='Tool A', version='1.0', url='http://example.com/tool-a')
    tool2 = Tool(name='Tool B', version='2.0', url='http://example.com/tool-b')

    tools_list.add_tool(tool1)
    tools_list.add_tool(tool2)

    print("All tools:", tools_list.filter_tools())
    tools_list.remove_tool('Tool A')
    print("After removing Tool A:", tools_list.filter_tools())
    print("Filtered tools by version 2.0:", tools_list.filter_tools(version='2.0'))
