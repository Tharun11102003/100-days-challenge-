"""
Task: Find the Highest Altitude
Problem Statement: Given a list of integers representing changes in altitude during a hike, determine the highest altitude reached. The starting altitude is 0. Each integer in the list adds to or subtracts from the current altitude, and you need to track the highest altitude reached during the hike.

Steps:
    1.Input:
       ❖ A list of integers, altitudeChanges, representing changes in altitude.

    2.Process:
       ❖ Initialize two variables: highestAltitude and currentAltitude, both set to 0.
       ❖ Iterate through each element (change) in the list altitudeChanges:
       ❖ Add the current change to currentAltitude.
       ❖ Update highestAltitude to be the maximum of highestAltitude and currentAltitude.

    3.Output:
       ❖ The value of highestAltitude, representing the maximum altitude reached during the hike.
"""



class Solution:
    def largestAltitude(self, altitudeChanges):
        highestAltitude = 0
        currentAltitude = 0

        for change in altitudeChanges:
            currentAltitude += change
            highestAltitude = max(highestAltitude, currentAltitude)

        return highestAltitude

gain = [-5, 1, 5, 0, -7]
solution = Solution()
print(solution.largestAltitude(gain))  







#==========================================


