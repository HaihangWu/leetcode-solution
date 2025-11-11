class SummaryRanges {
        public: map < int, int > intervals;
        SummaryRanges(){
        }

        void addNum(int value) {
                int start = value, end = value;
                auto it = intervals.upper_bound(value);
                if (it != intervals.begin()){
                    auto previt = prev(it);
                    if (value <= previt->second) return;
                    if (value == (previt->second+1)){
                        start=previt->first;
                        end=value;
                        intervals.erase(previt);
                        };
                }

                if (it != intervals.end() & & value == it->first-1){
                    end = it->second;
                    intervals.erase(it);
                    }
                intervals[start] = end;

        }

        vector < vector < int >> getIntervals(){
                 vector < vector < int >> res;
                for (auto & p:intervals){
                    res.push_back({p.first, p.second});
                    }
                return res;
        }
};
