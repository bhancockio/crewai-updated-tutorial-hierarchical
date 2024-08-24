from click import prompt
from crewai import Agent
from tools.search_tools import SearchTools


class AINewsLetterAgents():
    def editor_agent(self):
        return Agent(
            role='Editor',
            goal='Oversee the creation of the AI Newsletter',
            backstory="""With a keen eye for detail and a passion for storytelling, you ensure that the newsletter
            not only informs but also engages and inspires the readers. """,
            allow_delegation=True,
            verbose=True,
            max_iter=60,
        )

    def news_fetcher_agent(self):
        return Agent(
            role='NewsFetcher',
            goal='Fetch the top AI news stories for the day',
            backstory="""As a digital sleuth, you scour the internet for the latest and most impactful developments
            in the world of AI, ensuring that our readers are always in the know.""",
            tools=[SearchTools.search_internet],
            verbose=True,
            allow_delegation=True,
            #max_retry_limit=2000
        )

    def news_analyzer_agent(self):
        return Agent(
            role='NewsAnalyzer',
            goal='Analyze each news story and generate a detailed markdown summary with proper Heading,Subheading,Bulletpoints and Conclusion about the topic',
            backstory="""With a critical eye and a knack for distilling complex information, you provide insightful
            analyses of AI news stories, making them accessible and engaging for our audience.""",
            tools=[SearchTools.search_internet],
            verbose=True,
            allow_delegation=True,
            max_rpm=60,
            #max_iter=240,
        )

    def newsletter_compiler_agent(self):
        return Agent(

                role="Editor",
    goal="Edit a given blog post to align with the writing style of the organization.",
    backstory=(
        "You are an editor who receives a blog post from the Content Writer. "
        "Your goal is to review the blog post to ensure that it follows journalistic best practices, "
        "provides balanced viewpoints when providing opinions or assertions, "
        "and also avoids major controversial topics or opinions when possible."
    ),
    system_template="""<|start_header_id|>system<|end_header_id|>
                    You are an Editor responsible for reviewing and refining blog posts to align with the organization's writing style. 
                    Your task is to ensure that the content adheres to journalistic standards, offers balanced viewpoints, and maintains a neutral tone where appropriate.{{ .System }}<|eot_id|>""",
    prompt_template="""<|start_header_id|>user<|end_header_id|>

                    Your task is to edit the provided blog post to ensure it aligns with the organization's writing style and journalistic best practices. Focus on the following aspects:

                    - **Writing Style**: Ensure the content matches the tone, voice, and style guidelines of the organization.
                    - **Balanced Viewpoints**: Review opinions and assertions to ensure they are balanced and well-supported by evidence.
                    - **Controversial Topics**: Identify and address any major controversial topics or opinions, ensuring the content remains neutral and respectful.
                    - **Clarity and Coherence**: Improve the overall clarity and coherence of the content, ensuring a smooth flow of ideas.
                    - **Grammar and Syntax**: Proofread for grammatical errors, punctuation, and syntax issues.

                    Provide feedback and suggestions for any areas that require further revision.{{ .Prompt }}<|eot_id|>""",
    response_template="""<|start_header_id|>assistant<|end_header_id|>

                        Here is the edited version of the blog post with suggestions for improvement:

                    - **Writing Style Adjustments**: [Details of adjustments made to align with the organization's style]
                    - **Balanced Viewpoints**: [Examples of how viewpoints were balanced]
                    - **Controversial Topics Addressed**: [Details of any controversial topics addressed]
                    - **Clarity and Coherence Improvements**: [Summary of improvements made]
                    - **Grammar and Syntax Corrections**: [List of corrections made]

                    Please review the suggestions and make any additional revisions as needed.{{ .Response }}<|eot_id|>""",

        allow_delegation=False,
        verbose=True,
        max_rpm=60,
        max_iter=60,
)