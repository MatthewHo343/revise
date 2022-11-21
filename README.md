# Writing Feedback Generation

This is a [Cohere](https://cohere.ai/) API powered contextualized writing feedback generation bot! 

It responds to questions in the cli or streamlit chat by understanding the context of the conversation and then answering based on examples of constructive criticism.

## Motivation

Over the past few weeks, I have edited many of my friends' personal statements for future opportunities (i.e. scholarships, MS programs, PhD programs, etc.). The process of editing is time-intensive and I wanted to find a way to make it more efficient. This gave me a great idea to experiment with language models to give constructive criticism. Since language models don't have a mechanism for determining truth, the scope of this tool is limited to writing that is self-contained. This means the bot will not verify the truth behind statements but how they are used to support the objective.

## Example 
![image](https://github.com/MatthewHo343/revise/blob/a41df1657077ce4048e7f6107f21b9b0c171bb24/example.png)

## Overview Video
Here is a quick [video](https://www.youtube.com/watch?v=DpOQpClVgCw&ab_channel=NickFrosst) demoing the project and talking about ways in which it can be improved.

## Installation and Demo Use

To use this library, you will need:
* A Cohere API key: sign up for a free key at [https://dashboard.cohere.ai/welcome/register](https://dashboard.cohere.ai/welcome/register?utm_source=github&utm_medium=content&utm_campaign=sandbox&utm_content=groundedqa).

1. Clone the repository.
2. Install all the dependencies
```sh
pip install -r requirements.txt
```
3. Try the demo by running the cli tool
```sh
python3 cli_demo.py --cohere_api_key <API_KEY>
```
4. (Optional) Run the streamlit demo:
In the cloned repository, create a folder ```.streamlit/```. Inside the folder, create a file called ```secrets.toml``` and insert the following: ```cohere_api_token = <<YOUR COHERE API KEY>>```. Then run the following command:
```sh
streamlit run streamlit_demo.py
```
