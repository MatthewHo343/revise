# Writing Feedback Generation

This is a [Cohere](https://cohere.ai/) API powered contextualized writing feedback generation bot! 

It responds to questions in the cli or streamlit chat by understanding the context of the conversation and then answering based on examples of constructive criticism.

## Motivation

Over the past few weeks, I have edited many of my friends' personal statements for future opportunities (i.e. scholarships, MS programs, PhD programs, etc.). 

## Example 
![image](https://user-images.githubusercontent.com/5508538/199503137-5cb0f15b-c4b5-4458-99d0-21918c0194ff.png)

## Overview Video
Here is a quick [video](https://www.youtube.com/watch?v=DpOQpClVgCw&ab_channel=NickFrosst) demoing the project and talking about ways in which it can be improved.

## Installation and Demo Use

To use this library, you will need:
* A Serp API key, which you can obtain by registering at https://serpapi.com/users/welcome.
* A Cohere API key: sign up for a free key at [https://dashboard.cohere.ai/welcome/register](https://dashboard.cohere.ai/welcome/register?utm_source=github&utm_medium=content&utm_campaign=sandbox&utm_content=groundedqa).
* (Optional) A Discord key, which is the Discord bot token obtained when creating and configuring a Discord bot. See [docs](https://discord.com/developers/docs/topics/oauth2) for more info.

1. Clone the repository.
2. Install all the dependencies
```sh
pip install -r requirements.txt
```
3. Try the demo by running the cli tool
```sh
python3 cli_demo.py --cohere_api_key <API_KEY> --serp_api_key <API_KEY>
```
4. (Optional) Run the discord bot demo:  
You can create a discord both with this functionality by creating a bot account with message read and write permissions at https://discord.com/developers then running the following command
```sh
python3 discord_bot.py --cohere_api_key <API_KEY> --serp_api_key <API_KEY> --discord_key <DISCORD_KEY>
```
