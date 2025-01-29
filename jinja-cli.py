# Script to run Jinja2 reading from template and parameter files
# - Note: Undefined Jinja variables will cause errors
# - Note: 'trim_blocks' and 'lstrip_block are forced to True


def render_template(template_filename, parameters_filename, whitespace, unset_variables, verbose):
    import os
    import json
    import yaml
    import sys
    from jinja2 import Template, StrictUndefined

    if os.path.exists(parameters_filename):
        filepath = parameters_filename
    else:
        workdir = os.getcwd()
        filepath = os.path.join(workdir, parameters_filename)

    try:
        file = open(filepath)
    except OSError as os_error:
        print(f"{os_error}", file=sys.stderr)
        sys.exit(1)

    params = None
    try:
        if verbose:
            print(f"trying to JSON load, {file.name}")
        params = json.load(file)
    except json.decoder.JSONDecodeError as json_decode_error:
        file.seek(0)  # return to beginning of file
        if verbose:
            print(f"trying to YAML load, {file.name}")
        try:
            params = yaml.safe_load(file)
        except yaml.YAMLError as yaml_error:
            print(f"Parameters file not valid JSON or YAML, {yaml_error}", file=sys.stderr)
    finally:
        file.close()

    # Read the template file
    if os.path.exists(template_filename):
        filepath = template_filename
    else:
        workdir = os.getcwd()
        filepath = os.path.join(workdir, template_filename)

    template = None
    try:
        file = open(filepath)
        template = file.read()
    except OSError as os_error:
        print(f"{os_error}", file=sys.stderr)
        sys.exit(1)

    if whitespace and unset_variables:
        j2_template = Template(template)
    elif whitespace:
        j2_template = Template(template, undefined=StrictUndefined)
    elif unset_variables:
        j2_template = Template(template, trim_blocks=True, lstrip_blocks=True)
    else:
        j2_template = Template(template, undefined=StrictUndefined, trim_blocks=True, lstrip_blocks=True)

    print(j2_template.render(params))


if __name__ == '__main__':
    import argparse

    arguments = None
    parser = argparse.ArgumentParser(description='Simple Jinja2 CLI tool')
    parser.add_argument('-t', '--template', type=str, default=None, help='template file', required=True)
    parser.add_argument('-p', '--parameters', type=str, default=None, help='parameters file', required=True)
    parser.add_argument('-w', '--whitespace', help='enable white-space controls', default=False, action='store_true')
    parser.add_argument('-u', '--unset', help='allow unset variables', default=False, action='store_true')
    parser.add_argument('-v', '--verbose', action='count', default=0)
    args = parser.parse_args()

    render_template(
        template_filename=args.template,
        parameters_filename=args.parameters,
        whitespace=args.whitespace,
        unset_variables=args.unset,
        verbose=args.verbose
    )

    exit(0)
