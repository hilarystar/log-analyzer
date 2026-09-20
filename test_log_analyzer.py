from log_analyzer import analyze_log

def test_log_counts():
    logs = """INFO User logged in
    WARNING Failed lodin attempt
    ERROR Database connection failed
    INFO User logged out"""

    counts, error_rate, errors = analyze_log(logs)
    print(counts)
    
    assert counts["INFO"] == 2
    assert counts["WARNING"] == 1
    assert counts["ERROR"] == 1