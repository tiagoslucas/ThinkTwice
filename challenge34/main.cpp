#include <stdio.h>
#include <vector>
#include <string.h>
#include <algorithm>
#include <map>
using namespace std;
 
int dp[10005][64][3] = {};
const int mod = 1000000;
int main(int argc, char** args) {
    freopen(args[1], "r+t", stdin);
    freopen("result.txt", "w+t", stdout);
    int n, m, x, y;
    int cases = 0;
        scanf("%d %d", &n, &m);
        vector< pair<int, int> > D;
        map<int, int> R;
        for (int i = 0; i < n; i++) {
            scanf("%d %d", &x, &y);
            R[y] = 0;
            D.push_back(make_pair(x, y));
        }
        sort(D.begin(), D.end());
        int v = 0;
        for (map<int, int>::iterator it = R.begin();
            it != R.end(); it++)
            it->second = v++;
        for (int i = 0; i < n; i++)
            D[i].second = R[D[i].second];
        memset(dp, 0, sizeof(dp));
        int used[10005] = {};
        for (int i = 0; i < n; i++) {
            if (used[D[i].second] == 0) {
                dp[i][0][0] = 1; // =
                dp[i][0][1] = 1; // <
                dp[i][0][2] = 1; // > next time
                used[D[i].second] = 1;
            }
        }
        int ret = 0;
        if (m == 0)
            ret++;
        for (int i = 0; i < n; i++) {
            ret = (ret + dp[i][m][0])%mod;
            memset(used, 0, sizeof(used));
            for (int j = i+1; j < n; j++) {                
                if (used[D[j].second])  continue;
                used[D[j].second] = 1;
                for (int k = 0; k <= m; k++) {
                    if (D[j].second > D[i].second) { // larger
                        dp[j][k][0] = (dp[j][k][0] + dp[i][k][2])%mod;
                        dp[j][k+1][1] = (dp[j][k+1][1] + dp[i][k][2])%mod;
                        dp[j][k][2] = (dp[j][k][2] + dp[i][k][2])%mod;
                    } else if (D[j].second == D[i].second) {
                    } else {
                        dp[j][k][0] = (dp[j][k][0] + dp[i][k][1])%mod;
                        dp[j][k][1] = (dp[j][k][1] + dp[i][k][1])%mod;
                        dp[j][k+1][2] = (dp[j][k+1][2] + dp[i][k][1])%mod;
                    }
                }
            }
        }
        printf("%d\n",  ret);
   
    return 0;
}
