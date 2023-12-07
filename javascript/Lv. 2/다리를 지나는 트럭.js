function solution(bridgeLength, weight, truckWeights) {
  let result = 0;
  let bridgeWeights = truckWeights[0];
  let q = [[truckWeights.shift(), 0]];

  while (q.length > 0) {
    q.forEach((_, index, self) => (self[index][1] += 1));

    if (q[0][1] >= bridgeLength) bridgeWeights -= q.shift()[0];

    if (bridgeWeights + truckWeights[0] <= weight) {
      bridgeWeights += truckWeights[0];
      q.push([truckWeights.shift(), 0]);
    }

    result++;
  }

  return result + 1;
}
