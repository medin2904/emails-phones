#! python3
import re, pyperclip

# Create a regex for phone numbers
phoneRegex = re.compile(r''' ( 
((\d\d\d)|(\(\d\d\d\)))    # land area or telephone company dial
(\s|-)        # separator0
\d\d\d        # first 3 digits
(\s|-)        # separator
(\d\d\d(\d)?)        # last 3 -or- digits
(((ext(\.)?\s)|x)        # extension word-part (optional)
    (\d{2-5}))?        # extension number-part (optional)
)
''', re.VERBOSE)

# Create a regex for email addresses
emailRegex = re.compile('''
[a-zA-Z0-9_.]+      # prefix part
@        # @ symbol
[a-zA-Z0-9_.]+        # domain name part

''', re.VERBOSE)

# Get the text off the clipboard
text = pyperclip.paste()

# Extract the email/phone from this text
extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)

allPhoneNumbers = []
for phoneNumber in extractedPhone:
    allPhoneNumbers.append(phoneNumber[0])

# Copy the extracted email/phone to the clipboard
results = '\n'.join(allPhoneNumbers) + '\n' + '\n'.join(extractedEmail)
pyperclip.copy(results)
