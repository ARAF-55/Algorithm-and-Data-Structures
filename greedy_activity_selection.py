activities = [["A1", 0, 6],
              ["A2", 3, 4],
              ["A3", 1, 2],
              ["A4", 5, 8],
              ["A5", 5, 7],
              ["A6", 8, 9]
              ]


def printMaxActivities(activities_list):
    activities_list.sort(key=lambda x: x[2])
    i = 0
    firstA = activities_list[i][0]
    print(firstA)
    for j in range(len(activities_list)):
        if activities_list[j][1] > activities_list[i][2]:
            print(activities_list[j][0])
            i = j


printMaxActivities(activities)