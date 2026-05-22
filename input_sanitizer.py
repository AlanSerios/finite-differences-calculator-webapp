import re

def sanitize_function(func_str):
    """
    Validates a function string against a whitelist of allowed tokens.
    """
    if not func_str or not func_str.strip():
        raise ValueError("Function string cannot be empty.")
        
        
            
    # Remove all whitespace for easier validation and make lowercase
    cleaned_str = re.sub(r'\s+', '', func_str).lower()
    
    # Regex pattern to match allowed tokens
    pattern = re.compile(
        r'\b(?:x|sin|cos|tan|exp|log|ln|sqrt|abs|pi|e)\b|'  # variables and functions
        r'\d+\.\d+|\.\d+|\d+|'                          # numbers
        r'\*\*|\^|[+\-*/()]'                            # operators
    )
    
    # Replace all allowed tokens with empty string
    remainder = pattern.sub('', cleaned_str)
    
    # If anything is left, it's an invalid character or token
    if remainder:
        raise ValueError(f"Invalid characters or formatting detected in function.")
        
    return cleaned_str.replace('^', '**')
