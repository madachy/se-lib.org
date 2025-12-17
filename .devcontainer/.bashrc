# Custom aliases for se-lib
alias ll='ls -lah'
alias gs='git status'
alias serve='mkdocs serve'
alias build='mkdocs build'
alias test='pytest'

# Auto-activate venv if it exists
if [ -f venv/bin/activate ]; then
    source venv/bin/activate
fi

echo "se-lib development environment loaded!"
