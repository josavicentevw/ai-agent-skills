#!/bin/bash

# Package individual skills as ZIP files for uploading to Claude.ai or API

SKILLS_DIR="skills"
OUTPUT_DIR="packaged-skills"

# Create output directory
mkdir -p "$OUTPUT_DIR"

# Function to package a skill
package_skill() {
    local skill_name=$1
    local skill_path="$SKILLS_DIR/$skill_name"
    
    if [ ! -d "$skill_path" ]; then
        echo "❌ Error: Skill not found: $skill_name"
        return 1
    fi
    
    echo "📦 Packaging skill: $skill_name"
    
    # Create ZIP file
    cd "$SKILLS_DIR" || exit 1
    zip -r "../$OUTPUT_DIR/${skill_name}.zip" "$skill_name" -x "*.DS_Store" "*/\__pycache__/*" "*/.git/*"
    cd ..
    
    echo "✅ Created: $OUTPUT_DIR/${skill_name}.zip"
}

# Check if specific skill was requested
if [ $# -eq 0 ]; then
    echo "Packaging all skills..."
    echo ""
    
    # Package all skills
    for skill in "$SKILLS_DIR"/*; do
        if [ -d "$skill" ]; then
            skill_name=$(basename "$skill")
            package_skill "$skill_name"
            echo ""
        fi
    done
else
    # Package specific skill
    package_skill "$1"
fi

echo "✨ Done! Packaged skills are in: $OUTPUT_DIR/"
echo ""
echo "To upload to Claude API:"
echo "  See: https://platform.claude.com/docs/en/build-with-claude/skills-guide"
echo ""
echo "To upload to Claude.ai:"
echo "  1. Go to Settings > Features"
echo "  2. Upload the ZIP file"
