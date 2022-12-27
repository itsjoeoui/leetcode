import java.util.HashMap;

/*
 * @lc app=leetcode id=981 lang=java
 *
 * [981] Time Based Key-Value Store
 */

// @lc code=start

class Data {
    public String value;
    public int timestamp;

    public Data(String value, int timestamp) {
        this.value = value;
        this.timestamp = timestamp;
    }
}

class TimeMap {
    private HashMap<String, ArrayList<Data>> tm;

    public TimeMap() {
        this.tm = new HashMap<String, ArrayList<Data>>();
    }

    public void set(String key, String value, int timestamp) {
        if (!this.tm.containsKey(key)) {
            this.tm.put(key, new ArrayList<Data>());
        }
        this.tm.get(key).add(new Data(value, timestamp));
    }

    public String get(String key, int timestamp) {
        if (!this.tm.containsKey(key)) {
            return "";
        }
        return this.binarySearch(this.tm.get(key), timestamp);
    }

    private String binarySearch(ArrayList<Data> arr, int time) {
        int lp = 0;
        int rp = arr.size() - 1;
        int rtn = -1;
        while (lp <= rp) {
            int mp = lp + (rp - lp) / 2;
            if (arr.get(mp).timestamp <= time) {
                rtn = mp;
                lp = mp + 1;
            } else {
                rp = mp - 1;
            }
        }
        if (rtn == -1) {
            return "";
        }
        return arr.get(rtn).value;
    }
}

/**
 * Your TimeMap object will be instantiated and called as such:
 * TimeMap obj = new TimeMap();
 * obj.set(key,value,timestamp);
 * String param_2 = obj.get(key,timestamp);
 */
// @lc code=end
