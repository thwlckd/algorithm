function solution(m, musicinfos) {
  const data = [];
  const result = { time: 0, title: '(None)' };

  musicinfos.forEach((music) => {
    const temp = music.split(',');

    data.push({
      time:
        Number(temp[1].split(':')[0]) * 60 +
        Number(temp[1].split(':')[1]) -
        (Number(temp[0].split(':')[0] * 60) + Number(temp[0].split(':')[1])),
      title: temp[2],
      info: temp[3].replace(/(C|D|F|G|A)#/g, (_, v) => v.toLowerCase()),
    });
  });

  m = m.replace(/(C|D|F|G|A)#/g, (_, v) => v.toLowerCase());

  for (const { time, title, info } of data) {
    let melody = '';

    for (let i = 0; i < time; i++) {
      melody += info[i % info.length];
    }

    if (melody.match(m) && result.time < time) {
      result.time = time;
      result.title = title;
    }
  }

  return result.title;
}
