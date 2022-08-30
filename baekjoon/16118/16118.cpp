#include <cstdio>
#include <vector>
#include <queue>
#include <utility>
using namespace std;
#define MMAX 100000
#define INF 0x7fffffff
#define NMAX 4000

class Step {
    public:
    int loc;
    int dis;
    int speed;

    public:
    Step(int loc, int dis, int speed=0)
        : loc(loc), dis(dis), speed(speed) {
    }

    bool operator< (const Step& other) {
        return dis > other.dis;
    }
};

vector<pair<int, int>> arr[NMAX+1];
int fox[NMAX+1];
int wolf[2][NMAX+1];
int n, m;

void get_fox() {
    priority_queue <Step, vector<Step>, less<void>> pq;
    Step s = Step(0, 0);
    pq.push(s);
    for(int i=0;i<n;i++)
        fox[i] = INF;
    fox[0] = 0;

    while(!pq.empty()) {
        Step cur = pq.top();
        pq.pop();
        if (cur.dis > fox[cur.loc])
            continue;

        for(int i=0;i<arr[cur.loc].size();i++) {
            pair<int, int> nxt = arr[cur.loc].at(i);
            int nxt_dis = cur.dis + nxt.second;
            if (nxt_dis >= fox[nxt.first])
                continue;

            fox[nxt.first] = nxt_dis;
            Step n = Step(nxt.first, nxt_dis);
            pq.push(n);
        }
    }
}

void get_wolf() {
    priority_queue <Step, vector<Step>, less<void>> pq;
    Step s = Step(0, 0, 0);
    pq.push(s);
    for(int i=0;i<n;i++)
        wolf[0][i] = wolf[1][i] = INF;
    wolf[0][0] = 0;

    while(!pq.empty()) {
        Step cur = pq.top();
        pq.pop();
        if (cur.dis > wolf[cur.speed][cur.loc])
            continue;

        for(int i=0;i<arr[cur.loc].size();i++) {
            pair<int, int> nxt = arr[cur.loc].at(i);
            int nxt_dis = cur.dis;
            int nxt_speed = 0;

            if (cur.speed == 0) {
                nxt_dis += nxt.second / 2;
                nxt_speed = 1;
            }
            if (cur.speed == 1)
                nxt_dis += nxt.second * 2;

            if (nxt_dis >= wolf[nxt_speed][nxt.first])
                continue;

            wolf[nxt_speed][nxt.first] = nxt_dis;
            Step n = Step(nxt.first, nxt_dis, nxt_speed);
            pq.push(n);
        }
    }
}

int main() {
    int a, b, c;
    int count = 0;
    scanf("%d %d", &n, &m);
    for(int i=0;i<m;i++) {
        scanf("%d %d %d", &a, &b, &c);
        arr[a-1].push_back(make_pair(b-1, c*2));
        arr[b-1].push_back(make_pair(a-1, c*2));
    }
    get_fox();
    get_wolf();
    for(int i=0;i<n;i++) {
        if (fox[i] < wolf[0][i] && fox[i] < wolf[1][i]) {
            count += 1;
        }
    }
    printf("%d\n", count);

    return 0;
}
