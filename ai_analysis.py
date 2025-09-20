
# ai_analysis.py
# Contains the function to analyze CVs using OpenAI's LLM API.

from openai import OpenAI

def analyze_cv(api_key, file_content, job_role, job_description):
    """
    Analyzes a CV using OpenAI's LLM and returns feedback and recommendations.
    Args:
        api_key (str): OpenAI API key.
        file_content (str): Extracted text from the CV.
        job_role (str): Target job role for the analysis.
        job_description (str): Optional job description for alignment.
    Returns:
        str: The analysis and recommendations from the LLM.
    """
    prompt = f"""Please analyze the following CV and provide constructive feedback.
    focus on the following aspects:
    1. get the name of the candidate, email and phone number if available,give it an atractive format
    2. skills presentation
    3. experience description
    4. specific improvements for {job_role if job_role else 'general job applications'}
    5. content clarity and impact
    {"6. Compare the CV to the following job description and suggest specific adjustments to better align with it:\n" + job_description if job_description else ""}
    
    resume content:
    {file_content}

    please provide your analysis in a clear, structured format with specific recommendations for improvement.
    """

    client = OpenAI(api_key=api_key)
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "you are an expert career reviewer whith years of experience in HR and recruitment."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=1000,
        temperature=0.7,
    )
    return response.choices[0].message.content
