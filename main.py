from dotenv import dotenv_values
from langchain.llms import OpenAI

if __name__ == '__main__':
    print('Welcome to LangChain Playground')
    config = dotenv_values(".env")

    # temperature from 0 to 1, 0 implies deterministic response, 1 gives creative response
    # default to text-davinci-003
    llm = OpenAI(openai_api_key=config["OPENAI_API_KEY"], temperature=0.9)
    prompt = """
        What would a good catchy and fancy name be for a github project?
    """

    # print(llm(prompt))

    result = llm.generate([prompt] * 5)
    for name in result.generations:
        print(name[0].text)

