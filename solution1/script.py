import csv

def read_spec_file(spec_file):
    with open(spec_file, 'r', encoding='utf-8') as f:
        spec = []
        for line in f:
            field_name, length = line.strip().split()
            spec.append((field_name, int(length)))
    return spec

def parse_fixed_width_file(fixed_width_file, spec):
    with open(fixed_width_file, 'r', encoding='utf-8') as f:
        data = []
        for line in f:
            record = []
            position = 0
            for field_name, length in spec:
                record.append(line[position:position + length].strip())
                position += length
            data.append(record)
    return data

def write_csv_file(csv_file, data, spec):
    with open(csv_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        headers = [field_name for field_name, _ in spec]
        writer.writerow(headers)
        writer.writerows(data)

if __name__ == "__main__":
    spec_file = 'spec.txt'
    fixed_width_file = 'input.txt'
    csv_file = 'output.csv'

    spec = read_spec_file(spec_file)
    data = parse_fixed_width_file(fixed_width_file, spec)
    write_csv_file(csv_file, data, spec)