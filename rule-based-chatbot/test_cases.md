# Test Cases for Rule-Based Chatbot

The following test cases were used to verify the chatbot's functionality.

| Test Case ID | User Input | Expected Response Category | Status |
|--------------|------------|----------------------------|--------|
| TC01 | Hi | Greeting | Pass |
| TC02 | hello | Greeting (Case insensitive) | Pass |
| TC03 | What is your name? | Introduction | Pass |
| TC04 | how are you | Status Check | Pass |
| TC05 | help | Guidance | Pass |
| TC06 | what is your purpose | Purpose | Pass |
| TC07 | random text | Default/Unknown | Pass |
| TC08 | bye | Exit | Pass |
| TC09 |    Hey    | Greeting (Trimming whitespace) | Pass |

## Manual Verification Log
1. **Greeting**: Input "hey" -> Chatbot responds with greeting.
2. **Case Sensitivity**: Input "HELLO" -> Chatbot responds correctly.
3. **Keyword Matching**: Input "Can you help me?" -> Chatbot identifies "help" and responds.
4. **Exit**: Input "quit" -> Chatbot says goodbye and terminates.
