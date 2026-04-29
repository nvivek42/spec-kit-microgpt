name=scripts/update-agent-context.sh
#!/usr/bin/env bash
# Add microgpt context file to the update list if missing.

CONTEXT_FILE=".microgpt/context/compile-rules.md"
AGENTS_FILE=".agents_list"

if [ ! -f "$CONTEXT_FILE" ]; then
  echo "Warning: $CONTEXT_FILE not found in repository root. Ensure the .microgpt/context files are present."
fi

if [ ! -f "$AGENTS_FILE" ]; then
  echo "Creating $AGENTS_FILE with microgpt entry"
  echo "microgpt:$CONTEXT_FILE" > $AGENTS_FILE
else
  if ! grep -q "microgpt" $AGENTS_FILE; then
    echo "microgpt:$CONTEXT_FILE" >> $AGENTS_FILE
    echo "Appended microgpt entry to $AGENTS_FILE"
  else
    echo "microgpt already present in $AGENTS_FILE"
  fi
fi
