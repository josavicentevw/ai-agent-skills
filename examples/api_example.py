"""
Example: Using the Code Analysis API with Claude
"""

import anthropic
import json
from pathlib import Path

# Initialize the client
client = anthropic.Anthropic(api_key="your-api-key-here")

def upload_skill(skill_path: str) -> str:
    """
    Upload a skill to Claude API.
    
    Args:
        skill_path: Path to the skill ZIP file
    
    Returns:
        Skill ID for use in conversations
    """
    with open(skill_path, "rb") as f:
        skill = client.skills.create(
            file=f,
            name=Path(skill_path).stem
        )
    
    print(f"✅ Skill uploaded: {skill.id}")
    return skill.id


def analyze_code_with_skill(skill_id: str, code_file: str):
    """
    Use the code-analysis skill to analyze a code file.
    
    Args:
        skill_id: The uploaded skill ID
        code_file: Path to the code file to analyze
    """
    with open(code_file, "r") as f:
        code_content = f.read()
    
    # Upload the code file to Claude
    file_upload = client.files.upload(
        file=open(code_file, "rb"),
        purpose="code_execution"
    )
    
    # Create message with code execution and skill
    response = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=4096,
        tools=[{"type": "code_execution_2025_08_25"}],
        container={
            "type": "code_execution_container",
            "skill_ids": [skill_id],
            "files": [file_upload.id]
        },
        messages=[{
            "role": "user",
            "content": f"Analyze the code quality in {code_file}. Provide a detailed report with specific recommendations."
        }],
        betas=[
            "code-execution-2025-08-25",
            "skills-2025-10-02",
            "files-api-2025-04-14"
        ]
    )
    
    # Extract and print the analysis
    for block in response.content:
        if hasattr(block, "text"):
            print(block.text)


def main():
    """Main example workflow."""
    
    # 1. Upload the code-analysis skill
    print("📦 Uploading code-analysis skill...")
    skill_id = upload_skill("packaged-skills/code-analysis.zip")
    
    # 2. Analyze a code file
    print("\n🔍 Analyzing code...")
    analyze_code_with_skill(skill_id, "example_code.py")
    
    print("\n✨ Analysis complete!")


if __name__ == "__main__":
    main()
