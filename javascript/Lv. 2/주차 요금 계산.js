function solution(fees, records) {
  const result = [];
  const cars = new Map();

  records.forEach((record) => {
    const [time, car] = record.split(' ');
    const temp = time.split(':');
    const minute = Number(temp[0]) * 60 + Number(temp[1]);

    cars.has(car)
      ? cars.set(car, [...cars.get(car), minute])
      : cars.set(car, [minute]);
  });

  [...cars].sort().forEach(([_, time]) => {
    let acc = 0;

    if (time.length % 2 === 1) {
      acc += 23 * 60 + 59 - time.pop();
    }

    for (let i = 0; i < time.length; i += 2) {
      acc += time[i + 1] - time[i];
    }

    result.push(
      acc <= fees[0]
        ? fees[1]
        : fees[1] + Math.ceil((acc - fees[0]) / fees[2]) * fees[3]
    );
  });

  return result;
}
