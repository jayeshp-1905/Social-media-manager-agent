import os
from dotenv import load_dotenv
from crewai import Agent, Task, Crew, Process
from langchain_community.tools import DuckDuckGoSearchRun

load_dotenv()

class SocialSphereEngine:
    def __init__(self):
        self.search_tool = DuckDuckGoSearchRun()

    def create_social_crew(self, topic, platform):
        # Define Agents
        researcher = Agent(
            role='Trend Hunter',
            goal=f'Find 3 viral hooks for {topic} on {platform}',
            backstory="You are a data-driven specialist who finds trending news.",
            tools=[self.search_tool],
            verbose=True
        )

        writer = Agent(
            role='Content Architect',
            goal=f'Write a viral {platform} post about {topic}',
            backstory="You are a master copywriter who knows how to get clicks.",
            verbose=True
        )

        # Define Tasks
        task1 = Task(
            description=f"Analyze the top 3 trends for {topic} today.",
            expected_output="A bulleted list of 3 viral trends.",
            agent=researcher
        )

        task2 = Task(
            description=f"Create a {platform} post using the trends found.",
            expected_output=f"A high-quality {platform} post with emojis.",
            agent=writer
        )

        # Assemble the Crew
        return Crew(
            agents=[researcher, writer],
            tasks=[task1, task2],
            process=Process.sequential
        )