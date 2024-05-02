// 참조 풀이
// 분당 시침/분침 한번씩 총 두번 만나는 규칙 이용
function solution(h1, m1, s1, h2, m2, s2) {
  // from 00:00:00 to h:m:s
  const getCrossTime = (h, m, s) => {
    const hourD = (h * 30 + m * 0.5 + s / 120) % 360;
    const minuteD = (m * 6 + s * 0.1) % 360;
    const secondD = (6 * s) % 360;
    let count = -1; // 00:00:00 -> 1분에 한번만 만남

    // 마지막 초침 겹치는 여부
    if (secondD >= minuteD) count++;
    if (secondD >= hourD) count++;

    count += (h * 60 + m) * 2; // 분당 2번씩 만남
    count -= h; // 59분 -> 0분 일때 분침과 만나지 않음
    if (h >= 12) count -= 2; // 11:59:59 -> 12:00:00 일때 2분간 한번만 만남 2+2-1-2=1

    return count;
  };

  let count = getCrossTime(h2, m2, s2) - getCrossTime(h1, m1, s1);
  if ((h1 === 0 || h1 === 12) && m1 === 0 && s1 === 0) count += 1; // 겹친 상태로 시작하는 경우

  return count;
}

// 실패 풀이
function solution(h1, m1, s1, h2, m2, s2) {
  function getTimeDiff(h1, m1, s1, h2, m2, s2) {
    return (h2 - h1) * 3600 + (m2 - m1) * 60 + (s2 - s1); // time diff to sec
  }

  const diff = getTimeDiff(h1, m1, s1, h2, m2, s2);
  const temp = getTimeDiff(0, 0, 0, h1, m1, s1);
  let hourD = ((1 / 120) * temp) % 360; // 1초에 시침 1/120도 움직
  let minuteD = (0.1 * temp) % 360; // 1초에 분침 0.1도 움직
  let secondD = (6 * temp) % 360; // 1초에 초침 6도 움직
  let beforeHourD = hourD;
  let beforeMinuteD = minuteD;
  let beforeSecondD = secondD;
  let count = 0;
  let tick = 0;

  if (hourD === secondD || minuteD === secondD) count++;

  while (tick < diff) {
    hourD = (1 / 120 + hourD) % 360;
    minuteD = (0.1 + minuteD) % 360;
    secondD = (6 + secondD) % 360;

    if (beforeHourD > beforeSecondD && hourD <= secondD) count++;
    if (beforeMinuteD > beforeSecondD && minuteD <= secondD) count++;
    if (beforeSecondD === 354 && beforeHourD > beforeSecondD) count++;
    if (beforeSecondD === 354 && beforeMinuteD > beforeMinuteD) count++;

    beforeHourD = hourD;
    beforeMinuteD = minuteD;
    beforeSecondD = secondD;
    tick++;
  }

  return count;
}
