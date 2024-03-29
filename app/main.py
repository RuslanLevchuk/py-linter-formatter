def format_linter_error(error: dict) -> dict:
    return {
        "line": error["line_number"],
        "column": error["column_number"],
        "message": error["text"],
        "name": error["code"],
        "source": "flake8"
    }


def format_single_linter_file(file_path: str, errors: list) -> dict:
    return {
        "errors":
            [
                {
                    "line": error["line_number"],
                    "column": error["column_number"],
                    "message": error["text"],
                    "name": error["code"],
                    "source": "flake8"
                }
                for error in errors if error["filename"] == file_path
            ],
        "path": file_path,
        "status": "failed"
    }


def format_linter_report(linter_report: dict) -> list:
    return [
        {
            "errors":
                [
                    {
                        "line": source_value["line_number"],
                        "column": source_value["column_number"],
                        "message": source_value["text"],
                        "name": source_value["code"],
                        "source": "flake8"
                    }
                    for source_value in source_values
                ],
            "path": source_key,
            "status": "passed" if len(source_values) == 0 else "failed"
        } for source_key, source_values in linter_report.items()
    ]
