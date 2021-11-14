import requests

url = 'https://raw.githubusercontent.com/elastic/examples/master/Common%20Data%20Formats/nginx_logs/nginx_logs'
response = requests.get(url)
txt = response.text.split(')"')

limiter = 30  # Ограничитель вывода результата

def extract_log_data(input):
    output = list()
    i = 0
    for each in input:
        remote_addr_idx = each.find(' - - ')
        remote_addr = each[:remote_addr_idx].strip('\n')
        request_type_start = each.find('"', remote_addr_idx)
        request_type_end = each.find(' ', request_type_start, request_type_start+5)
        request_type = each[request_type_start+1:request_type_end]
        requested_resource_end = each.find(' HTTP', request_type_end)
        requested_resource = each[request_type_end+1:requested_resource_end]
        tuple_output = remote_addr, request_type, requested_resource
        output.append(tuple_output)
        if i == limiter: break
        i += 1
    return output


output = extract_log_data(txt)
print(output)
