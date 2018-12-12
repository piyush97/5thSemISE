#include <stdio.h>
void dijkstra(int n, int source, int cost[10][10], int dist[])
{
  int i, j, u, visited[10], min, count;
  for (i = 1; i <= n; i++)
  {
    visited[i] = 0;
    dist[i] = cost[source][i];
  }
  count = 2;
  while (count < n)
  {
    min = 99;
    for (j = 1; j <= n; j++)
    {
      if ((dist[j] < min) && (!visited[j]))
      {
        min = dist[j];
        u = j;
      }
    }
    visited[u] = 1;
    count++;
    for (j = 1; j <= n; j++)
    {
      if (((dist[u] + cost[u][j]) < dist[j]) && (!visited[j]))
        dist[j] = dist[u] + cost[u][j];
    }
  }
}
void main()
{
  int i, j, n, source, cost[10][10], dist[10];
  printf("Enter the no of vertices\n ");
  scanf("%d", &n);
  printf("Enter the cost matrix\n");
  for (i = 1; i <= n; i++)
  {
    for (j = 1; j <= n; j++)
    {
      scanf("%d", &cost[i][j]);
    }
  }
  printf("Enter the source node\n");
  scanf("%d", &source);
  dijkstra(n, source, cost, dist);
  printf("Shortest path is :\n");
  for (i = 1; i <= n; i++)
  {
    if (i != source)
      printf("%d-->%d : Cost= %d\n", source, i, dist[i]);
  }
}
