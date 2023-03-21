function resolveAfter20Seconds(x) {
    return new Promise((resolve) => {
      setTimeout(() => {
        resolve(x);
      }, 2000);
    });
  }
  
  async function f1() {
    const x = await resolveAfter20Seconds(10);
    console.log(x); // 10
  }
  
  f1();
  