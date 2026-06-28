/**
 * Definition of Interval:
 * class Interval {
 * public:
 *     int start, end;
 *     Interval(int start, int end) {
 *         this->start = start;
 *         this->end = end;
 *     }
 * }
 */

class Solution {
public:
    int minMeetingRooms(vector<Interval>& intervals) {
        vector<int> starts;
        vector<int> ends;
        int n = intervals.size();
        for(int i=0;i< n;i++){
            starts.push_back(intervals[i].start);
            ends.push_back(intervals[i].end);
        }
        sort(starts.begin(), starts.end());
        sort(ends.begin(), ends.end());

        int s = 0;
        int e = 0;
        int rooms =0;
        int max_rooms = 0;
        while( s < n){
            if(starts[s] < ends[e]){
                rooms++;
                max_rooms = max(max_rooms, rooms);
                s++;
            }else{
                e++;rooms--;
            }
        }
        return max_rooms;
    }
};
