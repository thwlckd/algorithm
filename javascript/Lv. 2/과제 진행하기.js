function solution(plans) {
  const pendding = []; // [name, rest]
  const done = []; // name
  const tasks = plans
    .map(([name, start, playtime]) => {
      const [hour, minute] = start.split(':').map((v) => Number(v));

      return [name, hour * 60 + minute, Number(playtime)];
    })
    .sort((a, b) => a[1] - b[1]);

  tasks.push(['end-flag', Number.MAX_SAFE_INTEGER, Number.MAX_SAFE_INTEGER]);

  for (let i = 0; i < tasks.length - 1; i++) {
    let [name, start, playtime] = tasks[i];
    let restTime = tasks[i + 1][1] - start - playtime;

    if (restTime >= 0) {
      // 한번에 끝내는 경우
      done.push(name);

      while (pendding.length > 0) {
        const [pName, pRest] = pendding.pop();

        if (restTime >= pRest) {
          // 스택에서 꺼낸 과제 끝마침
          done.push(pName);
          restTime -= pRest;
          continue;
        }

        pendding.push([pName, pRest - restTime]);
        break;
      }
    } else {
      // 한번에 못 끝내면 스택에 넣음
      pendding.push([name, -restTime]);
    }
  }

  return done;
}
