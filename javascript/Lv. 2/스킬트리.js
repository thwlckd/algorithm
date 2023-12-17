function solution(skill, skill_trees) {
  let result = 0;

  for (const skill_tree of skill_trees) {
    const temp = skill_tree.split('').filter((v) => skill.includes(v));
    let flag = true;

    for (let i = 0; i < temp.length; i++) {
      if (temp[i] !== skill[i]) {
        flag = false;
        break;
      }
    }

    if (flag) result++;
  }

  return result;
}
