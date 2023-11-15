use rand::Rng;
use rand::rngs::StdRng;
use rand_core::SeedableRng;
use std::cmp::min;
use std::collections::BTreeSet;

/*

The first line of the input contains an integer T denoting the number of test cases that follow. For each test case:
The first line contains two space-separated integers F B, where:
F denotes the number of floors in the mystery dungeon.
B denotes your initial belly value.
The second line contains four space-separated integers N M S E, where:
N denotes the number of rooms in each floor of the mystery dungeon.
M denotes the number of hallways in each floor of the mystery dungeon.
S denotes the room number of the starting room for each floor.
E denotes the room number of the exit room for each floor.
The third line contains F space-separated integers K1 K2 … KF, denoting that the treasure on the ith floor is located at room Ki
For each of the next M lines, the ith line contains two space-separated integers Xi Yi, denoting that a hallway connects rooms Xi and Yi in each floor of the dungeon.

*/

struct DSU {
    p: Vec<usize>,
    sz: Vec<usize>,
    pub ccs: BTreeSet<usize>,
}

impl DSU {
    pub fn new(n: usize, mut p: Vec<usize>, mut sz: Vec<usize>) -> DSU {
        let mut ini = BTreeSet::<usize>::new();
        for i in 0..n {
            p[i] = i;
            sz[i] = 1;
            ini.insert(i);
        }
        DSU { p: p.clone(), sz: sz.clone(), ccs: ini }
    }

    pub fn find(&mut self, i: usize) -> usize {
        if self.p[i] == i {
            i 
        } else {
            self.p[i] = self.find(self.p[i]);
            self.p[i]
        }
    }

    pub fn union(&mut self, i: usize, j: usize) -> bool {
        let mut x = self.find(i);
        let mut y = self.find(j);
        if x == y {
            return false
        }
        if self.sz[x] < self.sz[y] {
            let tmp = x;
            x = y;
            y = tmp;
        }
        self.p[x] = x;
        self.p[y] = x;
        self.sz[x] += self.sz[y];
        self.ccs.remove(&y);
        return true
    }
}

fn gen(maxn: usize, maxf: usize, maxb: usize) {
    let mut rng: StdRng = SeedableRng::from_entropy();
    // let mut file = File::create("sec.in");

    let mut edges : BTreeSet<(usize, usize)> = BTreeSet::new();
    let mut treas : BTreeSet<usize> = BTreeSet::new();
    let n = rng.gen_range(maxn/5*4..maxn+1);
    let m = rng.gen_range(n-1..maxn+1);
    let f = rng.gen_range(maxf/20*17..min(maxf,n)+1);
    let b = rng.gen_range(f..maxb+1);
    let s = rng.gen_range(1..n+1);
    let mut e = s;
    while e == s {
        e = rng.gen_range(1..n+1);
    }
    print!("{} {}\n", f, b);
    print!("{} {} {} {}\n", n, m, s, e);

    let mut vec = Vec::new(); 

    for _ in 0..f {
        let mut u = rng.gen_range(1..n+1);
        while treas.contains(&u) {
            u = rng.gen_range(1..n+1);
        }
        vec.push(u);
        treas.insert(u);
    }

    for i in 0..f {
        print!("{} ", vec[i]);
    }
    
    let mut p = Vec::<usize>::new();
    let mut sz = Vec::<usize>::new();
    p.resize(n+5, 0);
    sz.resize(n+5, 0);
    let mut dsu : DSU = DSU::new(n, p, sz);
    for _ in 0..n-1 {
       let mut b = rng.gen_range(1..n+1);
       let mut a = rng.gen_range(0..b);
       while dsu.find(b) == dsu.find(a) {
           b = rng.gen_range(1..n);
           a = rng.gen_range(0..b);
       }
       println!("{} {}", a, dsu.find(b));
       edges.insert((dsu.find(a), dsu.find(b)));
       dsu.union(a, b);
    }

    

    for _ in n..m+1 {
       let mut b = rng.gen_range(1..n+1);
       let mut a = rng.gen_range(0..b);
       while edges.contains(&(a, b)) || edges.contains(&(b, a)) {
            b = rng.gen_range(1..n+1);
            a = rng.gen_range(0..b);
       }
       edges.insert((a, b));
       println!("{} {}", a, b);
    }
}

fn main() {
    // customize this
    let t = 1;
    println!("{}", t);
    for _ in 0..t {
        // customize these
        gen(100000, 1000, 1000);
    }
    // too lazy for io prompt
}
