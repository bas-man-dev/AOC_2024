#!/usr/bin/python

with open('../input.txt', 'r') as all_reports:
    for reports in all_reports:
        reports = list(reports.split())
        #print(reports)
        print("next reports")
        for report in range(len(reports) - 1):
            print(reports[report], reports[report+1], " ", reports[report] == reports[report+1])