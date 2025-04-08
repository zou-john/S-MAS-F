#!/usr/bin/env python3
import argparse
from datetime import datetime
import os

from prompts import make_environment_prompt
from frameworks import make_langgraph


def main():
    # create the argument parser
    parser = argparse.ArgumentParser(description='Running Scenario On Desired Multi Agent Framework')
    
    # add arguments (fixed typos and improved the implementation)
    parser.add_argument('-f', '--framework', 
                       default='langchain',
                       help='Specify the multi-agent framework to use (default: langchain)')
    
    # generate default output directory based on current date and time
    default_output_dir = f"outputs/output_{datetime.now().strftime('%Y-%m-%d')}"
    
    parser.add_argument('-o', '--outputdir', 
                       default=default_output_dir,
                       help='Specify the output directory (default: automatically generated with timestamp)')
    
    parser.add_argument('-l', '--basellm', default='open-ai')

    parser.add_argument('-fp', '--filepaths', default=[], help='Please provide a filepath, if there are mutiple then separate it by , (comma)')
    
    list_of_files = args.filepaths.split(',') if args.filepaths else []

    
    # parse the arguments
    args = parser.parse_args()
    
    # print the values (or use them in your script)
    print(f"Running with framework: {args.framework}")
    print(f"With base llm: {args.basellm}")
    print(f"Analyzing the following files: {', '.join(list_of_files)}")  
    print(f"Output directory: {args.outputdir}")

    # create output directory if it doesn't exist
    os.makedirs(args.outputdir, exist_ok=True)
    
    # make the environment prompt
    environment_prompt = make_environment_prompt()

    workflow = make_langgraph()

if __name__ == '__main__':
    main()