function solution(record) {
  const nickname = {};
  const move = [];

  record.forEach((data) => {
    const [action, id, name] = data.split(' ');

    if (['Enter', 'Leave'].includes(action)) move.push({ action, id });

    if (name) nickname[id] = name;
  });

  return move.map(({ action, id }) =>
    action === 'Enter'
      ? `${nickname[id]}님이 들어왔습니다.`
      : `${nickname[id]}님이 나갔습니다.`
  );
}
