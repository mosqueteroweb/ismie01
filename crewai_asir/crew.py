from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task

@CrewBase
class AsirCurriculumCrew:
    """ASIR Curriculum Documentation Crew"""

    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    def __init__(self, output_dir: str, ra_number: str):
        super().__init__()
        self.output_dir = output_dir
        self.ra_number = ra_number

        # Conexión al LLM local (LM Studio / Ollama compatible) proporcionada por el usuario
        self.lmstudio_llm = LLM(
            model="openai/qwen2.5-7b-instruct",
            base_url="http://192.168.7.195:1234/v1",
            api_key="lm-studio"
        )

    @agent
    def curriculum_researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['curriculum_researcher'],
            llm=self.lmstudio_llm,
            verbose=True
        )

    @agent
    def theory_writer(self) -> Agent:
        return Agent(
            config=self.agents_config['theory_writer'],
            llm=self.lmstudio_llm,
            verbose=True
        )

    @agent
    def practical_instructor(self) -> Agent:
        return Agent(
            config=self.agents_config['practical_instructor'],
            llm=self.lmstudio_llm,
            verbose=True
        )

    @agent
    def assessment_evaluator(self) -> Agent:
        return Agent(
            config=self.agents_config['assessment_evaluator'],
            llm=self.lmstudio_llm,
            verbose=True
        )

    @task
    def research_curriculum_task(self) -> Task:
        return Task(
            config=self.tasks_config['research_curriculum_task'],
        )

    @task
    def write_theory_task(self) -> Task:
        # Dynamic output file path configuration
        return Task(
            config=self.tasks_config['write_theory_task'],
            output_file=f"{self.output_dir}/Teoria_{self.ra_number}.md"
        )

    @task
    def design_labs_task(self) -> Task:
        return Task(
            config=self.tasks_config['design_labs_task'],
            output_file=f"{self.output_dir}/Practicas_{self.ra_number}.md"
        )

    @task
    def create_assessment_task(self) -> Task:
        return Task(
            config=self.tasks_config['create_assessment_task'],
            output_file=f"{self.output_dir}/Evaluacion_{self.ra_number}.md"
        )

    @crew
    def crew(self) -> Crew:
        """Creates the ASIR Curriculum Documentation crew"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )
