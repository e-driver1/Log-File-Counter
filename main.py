def logCounting():
    file_path = "file.log"

    line_count = 0
    critical_count = 0
    error_count = 0
    warning_count = 0
    info_count = 0

    with open(file_path, "r") as file:
        for line in file:
            line_count += 1
            if "CRITICAL" in line:
                critical_count += 1
            if "ERROR" in line:
                error_count += 1
            if "WARNING" in line:
                warning_count += 1
            if "INFO" in line:
                info_count += 1

    # close file
    file.close()

    #print results
    print("Number of lines in the log file: ", line_count)
    print("Number of CRITICALS: ", critical_count)
    print("Number of ERRORS: ", error_count)
    print("Number of WARNINGS: ", warning_count)
    print("Number of INFOS: ", info_count)

    return critical_count, error_count, warning_count, info_count

logCounting()