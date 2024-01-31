import re

def parse_request(valid_auth_tokens, requests):
    result = []
    for request_type, url in requests:
        # Extracting authentication token from URL
        token_match = re.search(r'(?<=token=)[\w]+', url)

        if token_match:
            auth_token = token_match.group()
            # Validating authentication token
            if auth_token in valid_auth_tokens:
            # For POST requests, check CSRF token
                if request_type == "POST":
                    csrf_match = re.search(r'(?<=csrf=)[a-zA-Z0-9]{8,}', url)
                    if csrf_match:
                        csrf_token = csrf_match.group()
                        result.append(f"VALID,{','.join(parse_url_parameters(url))},{csrf_token}")
                    else:
                        result.append("INVALID")
                else:
                    result.append(f"VALID,{','.join(parse_url_parameters(url))}")
            else:
                result.append("INVALID")
        else:
            result.append("INVALID")
    return result

def parse_url_parameters(url):
    parameters_match = re.search(r'(?<=\?)[^#]+', url)
    if parameters_match:
        parameters_str = parameters_match.group()
        parameters = parameters_str.split('&')
        return parameters
    return []
# Example usage:


if __name__ == "__main__":
    valid_auth_tokens = ["ah37j2ha483u", "safh34ywb0p5", "ba34wyi8t902"]

    requests = [
        ["GET", "https://example.com/?token=347sd6yk8iu2&name=alex"],
        ["GET", "https://example.com/?token=safh34ywb0p5&name=sam"],
        ["POST", "https://example.com/?token=safh34ywb0p5&name=alex"],
        ["POST", "https://example.com/?token=safh34ywb0p5&csrf=ak2sh32dy&name=chris"]
    ]
    result = parse_request(valid_auth_tokens, requests)
    print(result)