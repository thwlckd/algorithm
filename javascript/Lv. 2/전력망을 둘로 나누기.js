function solution(n, wires) {
  let result = 100;
  const tree = Array.from({ length: n + 1 }, () => []);

  wires.forEach(([node1, node2]) => {
    tree[node1].push(node2);
    tree[node2].push(node1);
  });

  function bfs(root, exception) {
    let count = 0;
    const q = [root];
    const visited = [];
    visited[root] = true;

    while (q.length > 0) {
      const i = q.pop();

      tree[i].forEach((node) => {
        if (node !== exception && !visited[node]) {
          visited[node] = true;
          q.push(node);
          count++;
        }
      });
    }

    return count;
  }

  wires.forEach(([node1, node2]) => {
    result = Math.min(result, Math.abs(bfs(node1, node2) - bfs(node2, node1)));
  });

  return result;
}
