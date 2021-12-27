# Script to run Jinja2 reading from template and parameter files
# - Note: Undefined Jinja variables will cause errors
# - Note: 'trim_blocks' and 'lstrip_block are forced to True

# TODO: 2021.12.27: sjfke: Improve filepath handling to not assume CWD.
# TODO: 2021.12.27: sjfke: Improve Error Reporting

def render_template(template_filename, parameters_filename, file_format):
    import os
    import json
    import yaml
    from jinja2 import Template, StrictUndefined

    workdir = os.getcwd()
    filepath = os.path.join(workdir, parameters_filename)

    # Read the parameter values using YAML or JSON
    with open(filepath) as file:
        if file_format == 'yaml_format':
            params = yaml.safe_load(file)
        else:
            params = json.load(file)

    # Read the template file
    filepath = os.path.join(workdir, template_filename)
    with open(filepath) as file:
        template = file.read()

    j2_template = Template(template, undefined=StrictUndefined, trim_blocks=True, lstrip_blocks=True)

    print(j2_template.render(params))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    import argparse

    arguments = None
    parser = argparse.ArgumentParser(description='Simple Jinja2 CLI tool')
    parser.add_argument('-tfile', type=str, default=None, help='template file', required=True)
    parser.add_argument('-pfile', type=str, default=None, help='parameters file', required=True)
    parser.add_argument('-j', '--json', help='JSON parameters file', default=False, action='store_true')
    parser.add_argument('-y', '--yaml', help='YAML parameters file', default=False, action='store_true')
    parser.add_argument('-v', '--verbose', action='count', default=0)
    args = parser.parse_args()

    if args.json:
        parameters_format = 'json_format'
    else:
        parameters_format = 'yaml_format'

    render_template(template_filename=args.tfile, parameters_filename=args.pfile, file_format=parameters_format)

    exit(0)
