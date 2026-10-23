# SC2005 Operating Systems — examination question bank

Prepared from the lecture slide decks in `SC2005_slides_recordings/`, `tut1.pdf`, the lab manuals, and the available quiz screenshots. The questions are original practice questions, not predictions of the actual paper. `Baka` means deliberately integrative and very difficult.

Each topic has 5 easy, 5 medium, 5 hard and 1 Baka MCQ, followed by 1 open-ended question at each level. MCQs include the answer so this can be used as a self-marking bank; open-ended items include marking points.

## 1. Introduction and OS foundations

### MCQ — Easy

1. The primary role of an operating system is to: (A) replace all application programs (B) act as an intermediary between users/applications and hardware (C) manufacture CPU instructions (D) eliminate I/O. **Ans: B**
2. Which is not one of the four broad components of a computer system? (A) Hardware (B) Operating system (C) Application programs (D) Compiler optimisations only. **Ans: D**
3. The kernel is best described as: (A) a user document (B) the core OS program that remains ready to handle requests and hardware events (C) a device cable (D) a batch job. **Ans: B**
4. A simple batch system can waste CPU time when the current job: (A) computes continuously (B) waits for I/O (C) terminates (D) is loaded. **Ans: B**
5. A real-time system is characterised mainly by: (A) unlimited memory (B) fixed timing constraints and deadlines (C) no interrupts (D) no hardware. **Ans: B**

### MCQ — Medium

6. Multiprogramming improves CPU utilisation primarily by: (A) running only one job (B) running another ready job while one job waits for I/O (C) removing memory management (D) disabling interrupts. **Ans: B**
7. Which OS function chooses among ready jobs for the CPU? (A) File organisation (B) CPU scheduling (C) Compilation (D) Linking. **Ans: B**
8. In a tightly coupled multiprocessor system, processors commonly communicate through: (A) shared memory (B) punched cards (C) separate keyboards only (D) the file extension. **Ans: A**
9. The main focus of a desktop OS is generally: (A) user convenience and responsiveness (B) guaranteeing every task a hard deadline (C) zero storage (D) no protection. **Ans: A**
10. A device controller usually: (A) executes application source code (B) controls a device and has a local buffer (C) replaces the kernel (D) schedules processes. **Ans: B**

### MCQ — Hard

11. The goals of convenience and efficient hardware use can conflict because: (A) convenience requires no hardware (B) sophisticated allocation may require information and overhead that reduce simplicity (C) hardware cannot run programs (D) users cannot issue commands. **Ans: B**
12. A CPU and an I/O device can operate concurrently because: (A) the device controller can transfer data through its buffer while the CPU executes (B) the CPU becomes part of the disk (C) I/O never needs memory (D) interrupts stop all execution permanently. **Ans: A**
13. Which combination best explains why multiprocessors can be more reliable? (A) redundancy and the possibility of continued service after one component fails (B) they have no shared resources (C) they require no OS (D) they never interrupt. **Ans: A**
14. A handheld OS must particularly account for: (A) unlimited battery and display size (B) limited memory, processing power and display area (C) absence of users (D) only batch workloads. **Ans: B**
15. In a time-sharing system, swapping is used chiefly to: (A) keep several jobs available and support interactive users (B) prevent context switches (C) make all programs kernel code (D) remove the ready queue. **Ans: A**

### MCQ — Baka

16. An embedded controller must react within a deadline, share one CPU among multiple activities, and protect device state. Which OS design concern is most central? (A) maximising average batch throughput only (B) combining predictable scheduling, interrupt handling and protection under resource constraints (C) replacing all interrupts with polling only (D) maximising virtual address size regardless of timing. **Ans: B**

### Open-ended

- **Easy:** Define an operating system and state its two broad goals. **Key:** intermediary between users/applications and hardware; user convenience; efficient hardware utilisation/resource allocation.
- **Medium:** Explain how a simple batch system differs from a multiprogrammed/time-sharing system. **Key:** one job vs several in memory; automatic job sequencing vs interactive communication; CPU idle during I/O vs another job can run; need for memory/CPU/I/O scheduling.
- **Hard:** Explain why OS abstractions, policies and mechanisms are useful, and give one example of each. **Key:** abstraction hides complexity; policy decides what should happen; mechanism implements how; examples such as files/CPU scheduling policy/context-switch mechanism.
- **Baka:** Design a high-level OS strategy for a medical embedded controller that must meet deadlines but also log data and support updates. **Key:** hard/soft real-time distinction; priority/deadline scheduling; bounded interrupt and I/O paths; memory protection; isolation/update recovery; logging must not block critical work; explain trade-offs.

## 2. Processes and threads

### MCQ — Easy

1. A process is: (A) a program in execution (B) only source code (C) a disk sector (D) a CPU register. **Ans: A**
2. A process waiting for an I/O completion is in the: (A) running state (B) waiting/blocked state (C) new state (D) terminated state. **Ans: B**
3. The PCB normally stores: (A) only the file name (B) process state, program counter and registers among other information (C) monitor pixels (D) source comments only. **Ans: B**
4. A context switch requires the OS to: (A) save the old process context and load the new one (B) delete both processes (C) recompile the kernel (D) format the disk. **Ans: A**
5. A thread is best viewed as: (A) a unit of execution within a process (B) a disk partition (C) a directory entry (D) a page table entry. **Ans: A**

### MCQ — Medium

6. A process in the ready state is: (A) executing on a CPU (B) able to execute but waiting for CPU allocation (C) waiting for a disk only (D) already terminated. **Ans: B**
7. The short-term scheduler selects from the: (A) disk job pool only (B) ready queue (C) file directory (D) interrupt vector only. **Ans: B**
8. The long-term scheduler mainly controls: (A) the degree of multiprogramming by admitting jobs to memory (B) each instruction’s arithmetic (C) file names (D) page offsets. **Ans: A**
9. The medium-term scheduler is associated with: (A) swapping partially executed processes out and back in (B) compiling source code (C) choosing a file’s extension (D) handling only keyboard input. **Ans: A**
10. If a parent calls `wait()` after creating a child, the parent generally: (A) waits for child termination/status (B) becomes a kernel thread permanently (C) deletes the child immediately (D) bypasses the PCB. **Ans: A**

### MCQ — Hard

11. A context switch is overhead because during the switch: (A) no useful user-process work is performed (B) the CPU is destroyed (C) all memory is erased (D) the new process cannot ever run. **Ans: A**
12. In a many-to-one user-thread model, a blocking system call by one user thread can: (A) block the entire process because the kernel sees one schedulable thread (B) block no one (C) create a new CPU (D) guarantee parallelism. **Ans: A**
13. If a child performs `exec` after `fork`, the usual effect is that it: (A) replaces its process image with a new program (B) becomes the parent’s PCB (C) changes only its PID (D) terminates before loading code. **Ans: A**
14. A zombie process is one that: (A) is still running invisibly (B) has exited but remains in the process table until its status is collected (C) has never been created (D) owns no PID. **Ans: B**
15. On one core with preemptive Round Robin, when a quantum expires, the running process normally moves to: (A) ready, unless it has terminated or blocked (B) new only (C) terminated always (D) the file queue. **Ans: A**

### MCQ — Baka

16. A parent creates a child at t=0; the child immediately sends a blocking IPC message at t=6; the parent’s CPU quantum expires at t=7. Assuming the child was made ready by the send and the scheduler runs immediately, which event must be true? (A) the child cannot run until the parent exits (B) the child can enter the ready queue before t=7 and may be selected at the next scheduling opportunity (C) the parent remains running despite blocking (D) `fork` makes both processes share one PCB. **Ans: B**

### Open-ended

- **Easy:** Draw the five basic process states and explain the ready-to-running and running-to-waiting transitions. **Key:** new, ready, running, waiting, terminated; scheduler dispatches ready→running; I/O/event request causes running→waiting.
- **Medium:** Explain the contents of a PCB and why each of the program counter, registers and memory-management information is needed during a context switch. **Key:** identify fields; PC resumes next instruction; registers restore execution state; base/limit or equivalent protects/translates memory; state and scheduling data choose/resume process.
- **Hard:** Compare long-, medium- and short-term schedulers in trigger frequency, input/output and purpose. **Key:** long-term disk→memory and admission, infrequent; short-term ready queue→CPU, frequent; medium-term swap out/in under load; degree of multiprogramming.
- **Baka:** Analyse a `fork`/`wait`/IPC process tree in which the parent and child have different CPU quanta and one blocks on receive. State possible process-state transitions and explain why exact execution order may be nondeterministic. **Key:** separate PCBs/address spaces; scheduler/preemption; blocking receive; wake-up on send; parent may wait or run; race/order depends on timing and queue policy.

## 3. CPU scheduling and algorithms

### MCQ — Easy

1. FCFS scheduling is normally: (A) nonpreemptive (B) always preemptive (C) random (D) disk-only. **Ans: A**
2. Round Robin is defined by a: (A) time quantum (B) page size (C) file inode (D) base register only. **Ans: A**
3. SJF chooses the process with the smallest predicted: (A) CPU burst (B) PID (C) file name (D) page number. **Ans: A**
4. Throughput is the number of processes completed per: (A) unit time (B) page (C) context switch (D) byte. **Ans: A**
5. Response time ends when a process: (A) first enters running (B) terminates (C) finishes all I/O (D) is admitted to disk. **Ans: A**

### MCQ — Medium

6. FCFS’s convoy effect means: (A) short jobs wait behind a long job (B) every job has the same burst (C) pages convoy in memory (D) all jobs run simultaneously. **Ans: A**
7. SRTF is the preemptive version of: (A) SJF (B) FCFS (C) multilevel feedback only (D) FIFO page replacement. **Ans: A**
8. Increasing a Round Robin quantum until it is very large makes RR approach: (A) FCFS (B) SRTF (C) optimal paging (D) priority inversion. **Ans: A**
9. Waiting time is calculated as turnaround time minus: (A) CPU bursts and I/O/event-wait time (B) PID (C) response time only (D) arrival time only. **Ans: A**
10. A preemptive scheduler may take the CPU from a running process: (A) before it voluntarily blocks or terminates (B) only after termination (C) only during boot (D) never. **Ans: A**

### MCQ — Hard

11. P1, P2, P3 arrive at 0 with burst lengths 8, 4, 2. Nonpreemptive SJF’s average waiting time is: (A) 2 (B) 4 (C) 6 (D) 14/3. **Ans: A** (order P3,P2,P1; waits 0,2,6)
12. For FCFS order P1(5), P2(3), P3(2), all at 0, the average waiting time is: (A) 13/3 (B) 3 (C) 5 (D) 10. **Ans: A**
13. With RR quantum 2 and ready queue P1(5), P2(3), both at 0, after P1’s first slice the next process is: (A) P2 (B) P1 again (C) neither (D) a new process. **Ans: A**
14. A scheduler that prioritises short jobs minimises average waiting time under the standard assumptions because: (A) completing short bursts earlier reduces time imposed on later jobs (B) it eliminates all context switches (C) it guarantees no starvation (D) it ignores arrivals. **Ans: A**
15. On a two-core system, CPU utilisation is total busy core-time divided by: (A) elapsed time × 2 (B) elapsed time only (C) number of processes (D) quantum. **Ans: A**

### MCQ — Baka

16. P1 arrives at 0 with burst 7; P2 at 2 with burst 3; P3 at 4 with burst 1. Under SRTF, which execution sequence is correct (ignoring switch cost)? (A) P1(0–2), P2(2–4), P3(4–5), P2(5–6), P1(6–11) (B) P1(0–7), P2, P3 (C) P3 first, P2, P1 (D) P1(0–2), P3(2–3), P2(3–6), P1. **Ans: A**

### Open-ended

- **Easy:** Define turnaround, waiting and response time. **Key:** admission/arrival to termination; time in ready queue; admission/arrival to first running.
- **Medium:** Compute the FCFS and nonpreemptive-SJF schedules and average waiting time for P1=6, P2=2, P3=4, all arriving at 0. **Key:** FCFS order P1,P2,P3, waits 0,6,8, average 14/3; SJF order P2,P3,P1, waits 0,2,6, average 8/3.
- **Hard:** Explain the trade-off when choosing a Round Robin quantum. **Key:** small quantum improves response/fairness but increases context-switch overhead; large quantum reduces overhead but approaches FCFS and harms response; workload and switch cost matter.
- **Baka:** Given an arrival/burst table, compare FCFS, SJF, SRTF and RR, showing Gantt charts, waiting/turnaround/response times, and one fairness/starvation observation. **Key:** correct event-by-event schedule; definitions and arithmetic; explain preemption on arrivals; identify SJF starvation risk and RR fairness/overhead.

## 4. Process synchronization

### MCQ — Easy

1. A race condition occurs when the result depends on: (A) the timing/interleaving of concurrent accesses (B) file extension only (C) page size only (D) CPU brand. **Ans: A**
2. The part of a program accessing shared data is the: (A) critical section (B) boot sector (C) ready queue (D) text file. **Ans: A**
3. Mutual exclusion means: (A) at most one process is in a critical section at a time (B) no process can run (C) all processes run together (D) every lock is recursive. **Ans: A**
4. A semaphore wait operation generally: (A) decrements/claims a permit and may block (B) always increments (C) deletes the semaphore (D) disables memory. **Ans: A**
5. A binary semaphore used for mutual exclusion is commonly initialised to: (A) 1 (B) 0 always (C) -1 (D) the page size. **Ans: A**

### MCQ — Medium

6. The three classic critical-section requirements are: (A) mutual exclusion, progress and bounded waiting (B) paging, swapping and linking (C) throughput, disk and files (D) fork, exec and exit. **Ans: A**
7. In a bounded buffer, `empty` counts: (A) unused slots (B) filled slots (C) CPUs (D) waiting processes only. **Ans: A**
8. A producer should normally wait for `empty` before entering the buffer’s critical update because: (A) it must not insert into a full buffer (B) it must avoid all CPU use (C) it is a consumer (D) it needs a page fault. **Ans: A**
9. A mutex lock is released by: (A) the owner after leaving the critical section (B) any unrelated process at any time (C) the disk controller (D) the compiler only. **Ans: A**
10. A monitor provides: (A) mutual exclusion around its procedures plus condition synchronisation (B) only a disk cache (C) no shared state (D) CPU scheduling only. **Ans: A**

### MCQ — Hard

11. If a process executes `wait(mutex)` twice without a matching signal and mutex starts at 1, it will most likely: (A) block on the second wait (B) enter twice safely (C) increment the value (D) terminate normally. **Ans: A**
12. In a bounded-buffer solution, the usual semaphore wait order `wait(empty); wait(mutex)` prevents: (A) a producer holding the mutex while waiting for space, which could block consumers from freeing space (B) all mutual exclusion (C) the buffer from ever filling (D) page replacement. **Ans: A**
13. If two increments are implemented as read–modify–write and interleave, the final value can lose an update because: (A) both processes can read the same old value (B) the CPU cannot add 1 (C) the variable is immutable (D) interrupts cannot occur. **Ans: A**
14. Busy waiting differs from blocking because a busy-waiting process: (A) repeatedly checks while consuming CPU (B) is always terminated (C) is swapped to disk immediately (D) cannot be preempted. **Ans: A**
15. A correct lock-free-looking algorithm that violates bounded waiting may cause: (A) starvation (B) a file rename (C) a page hit (D) compilation. **Ans: A**

### MCQ — Baka

16. Producer code is `wait(mutex); wait(empty); insert(); signal(empty); signal(mutex)`, consumer code is `wait(mutex); wait(full); remove(); signal(full); signal(mutex)`. If the buffer is full, what can happen? (A) producer holds mutex waiting for empty while consumer cannot acquire mutex to remove, causing deadlock (B) it is always correct (C) only the consumer starves but never deadlocks (D) the buffer becomes empty automatically. **Ans: A**

### Open-ended

- **Easy:** Explain race condition and critical section using a shared counter. **Key:** concurrent read–modify–write; different interleavings yield different final counts; counter update is critical section.
- **Medium:** Write semaphore pseudocode for a bounded buffer of size N and explain `empty`, `full` and `mutex`. **Key:** producer waits empty/mutex, inserts, signals mutex/full; consumer waits full/mutex, removes, signals mutex/empty; initial values N, 0, 1.
- **Hard:** Show how incorrect semaphore order can deadlock the bounded-buffer solution. **Key:** producer/consumer each hold mutex then wait on unavailable resource; opposite party needs mutex to create that resource; demonstrate cycle; correct order releases/claims counting semaphore before mutex.
- **Baka:** Compare mutex, binary semaphore, counting semaphore and monitor for a shared resource with multiple conditions. **Key:** ownership vs permit semantics; counting capacity; monitor encapsulation and condition variables; waking semantics; misuse and deadlock risks; justify a design.

## 5. Deadlocks and starvation

### MCQ — Easy

1. A deadlock is a state where processes: (A) wait forever for events/resources held by one another (B) all terminate (C) use no resources (D) execute only I/O. **Ans: A**
2. Which is a necessary deadlock condition? (A) mutual exclusion (B) infinite memory (C) zero processes (D) no waiting. **Ans: A**
3. Hold-and-wait means a process: (A) holds at least one resource while waiting for another (B) holds nothing (C) waits only after termination (D) releases everything before requesting. **Ans: A**
4. Starvation means: (A) indefinite postponement while other processes continue to progress (B) all processes are blocked in a cycle necessarily (C) memory is full (D) a process has terminated. **Ans: A**
5. A resource-allocation graph can represent: (A) processes, resources and request/assignment edges (B) only file names (C) CPU bursts only (D) page offsets. **Ans: A**

### MCQ — Medium

6. The four Coffman conditions are mutual exclusion, hold-and-wait, no preemption and: (A) circular wait (B) paging (C) response time (D) compilation. **Ans: A**
7. Deadlock prevention works by: (A) denying at least one necessary condition (B) increasing every queue (C) removing all processes (D) guaranteeing starvation. **Ans: A**
8. A safe state is one in which: (A) there exists an order allowing all processes to finish with available resources (B) a deadlock has occurred (C) no resources are allocated (D) all processes are terminated. **Ans: A**
9. Banker’s algorithm grants a request only if the resulting state is: (A) safe (B) necessarily fastest (C) empty (D) preemptive. **Ans: A**
10. Deadlock detection differs from prevention because detection: (A) allows deadlock to occur and then searches for it (B) forbids all resource requests (C) applies only to files (D) eliminates scheduling. **Ans: A**

### MCQ — Hard

11. If P1 holds R1 and requests R2 while P2 holds R2 and requests R1, the graph contains: (A) a cycle and a deadlock under single-instance resources (B) no dependency (C) only starvation (D) a page fault. **Ans: A**
12. A safe sequence is best described as: (A) an ordering in which each process can obtain its remaining need and release resources (B) the order processes arrived (C) any CPU schedule (D) a list of terminated files. **Ans: A**
13. Requiring processes to request all resources before execution can prevent hold-and-wait but may cause: (A) low utilisation and possible starvation (B) guaranteed maximum throughput (C) no waiting at all (D) faster response always. **Ans: A**
14. If a process can be forcibly deprived of a resource without invalidating its work, allowing preemption can break: (A) no-preemption (B) mutual exclusion always (C) circular wait only (D) progress. **Ans: A**
15. A cycle in a resource-allocation graph proves deadlock: (A) when each resource type has one instance; with multiple instances it indicates possible deadlock (B) always, regardless of instances (C) never (D) only for files. **Ans: A**

### MCQ — Baka

16. Available=(3,2), Allocation P1=(1,0), P2=(1,1), P3=(1,0), Max P1=(2,1), P2=(1,2), P3=(3,1). Which is a safe sequence? (A) P1 then P2 then P3 (B) P2 then P1 then P3 (C) P3 then P2 then P1 (D) none. **Ans: A**

### Open-ended

- **Easy:** State and explain the four necessary conditions for deadlock. **Key:** mutual exclusion, hold-and-wait, no preemption, circular wait; one-sentence explanation each.
- **Medium:** Distinguish deadlock, starvation and livelock. **Key:** deadlock: circular waiting/no progress; starvation: one waits indefinitely while system progresses; livelock: active state changes but no useful progress.
- **Hard:** Explain prevention, avoidance, detection/recovery and the trade-off of each. **Key:** prevention structurally breaks condition; avoidance uses future maximum claims/safe state; detection permits then finds; recovery preemption/rollback/termination; overhead vs utilisation.
- **Baka:** Run Banker’s algorithm on a supplied Allocation/Max/Available table, either approve or reject a request, and justify the result. **Key:** compute Need=Max−Allocation; simulate Work/Finish; safe sequence; then compare request to Need/Available; only commit if post-request state remains safe.

## 6. Real-time operating systems

### MCQ — Easy

1. A hard real-time task must: (A) meet its deadline or the result may be invalid (B) maximise average waiting time (C) avoid all interrupts (D) use virtual memory always. **Ans: A**
2. An example of a real-time control system is: (A) airbag control (B) text formatting only (C) offline archive compression (D) a directory listing. **Ans: A**
3. A deadline is: (A) the latest acceptable completion time (B) the process PID (C) a disk block (D) a page offset. **Ans: A**
4. RTOS design prioritises: (A) predictable timing (B) unlimited throughput only (C) large GUIs only (D) random scheduling. **Ans: A**
5. A sensor interrupt is generated by: (A) an external/device event (B) a linker (C) a file extension (D) a page table alone. **Ans: A**

### MCQ — Medium

6. In a hard real-time system, average response time is insufficient because: (A) a single missed deadline may be unacceptable (B) averages are always zero (C) deadlines do not exist (D) CPU bursts are impossible. **Ans: A**
7. A soft real-time task generally: (A) benefits from timely completion but tolerates occasional lateness (B) must never miss any deadline (C) cannot be preempted (D) cannot use I/O. **Ans: A**
8. To improve predictability, an RTOS may avoid: (A) unbounded blocking and unpredictable paging (B) all priority information (C) interrupts (D) timers. **Ans: A**
9. Priority inversion occurs when: (A) a high-priority task waits for a resource held by a low-priority task, while medium-priority work delays release (B) priorities are all equal (C) a page is replaced (D) a process exits. **Ans: A**
10. A timer is useful in RTOS scheduling because it: (A) provides a predictable preemption/deadline reference (B) stores file attributes (C) links libraries (D) allocates disk blocks. **Ans: A**

### MCQ — Hard

11. A feasible schedule requires each task to complete: (A) by its deadline under the assumed execution and release constraints (B) in PID order (C) after all lower-priority work (D) only at shutdown. **Ans: A**
12. A long nonpreemptible critical section is dangerous in RTOS because it can: (A) delay a higher-priority task past its deadline (B) reduce all memory use to zero (C) remove the timer (D) guarantee fairness. **Ans: A**
13. Priority inheritance addresses priority inversion by: (A) temporarily raising the resource holder’s priority (B) deleting the high-priority task (C) lowering every priority permanently (D) disabling resource protection. **Ans: A**
14. A periodic task with period T and deadline D needs analysis of: (A) worst-case execution time, release/period and deadline (B) filename and extension only (C) page table length only (D) directory depth only. **Ans: A**
15. An RTOS may sacrifice average throughput to: (A) guarantee bounded response and deadline behaviour (B) maximise fragmentation (C) increase deadlock (D) eliminate protection. **Ans: A**

### MCQ — Baka

16. A high-priority control task is released every 10 ms, has WCET 3 ms, and can be blocked for 8 ms by a lower-priority task; a medium task is always ready. Which design issue is most urgent? (A) priority inversion and blocking analysis may make the 10 ms deadline infeasible; use bounded critical sections/protocols (B) increase the medium task priority (C) disable all interrupts forever (D) use FCFS only. **Ans: A**

### Open-ended

- **Easy:** Distinguish hard and soft real-time systems with one example each. **Key:** hard deadline miss unacceptable; soft late result degrades service; examples airbag vs multimedia playback.
- **Medium:** Explain why predictability is often more important than peak throughput in an RTOS. **Key:** deadlines; worst-case rather than average; bounded interrupt/scheduling/locking delays; safety/correctness consequences.
- **Hard:** Explain priority inversion and two ways to mitigate it. **Key:** low-priority holder blocks high priority; medium task preempts holder; priority inheritance/ceiling; bound critical sections and blocking.
- **Baka:** Given periodic tasks with release times, WCETs and deadlines, construct or reject a priority schedule and identify the first missed deadline. **Key:** timeline; account for preemption, blocking and interrupt overhead; justify feasibility, not just average utilisation.

## 7. Virtualization

### MCQ — Easy

1. A virtual machine is an isolated duplicate of a: (A) real machine/system (B) file name (C) page offset (D) semaphore. **Ans: A**
2. The hypervisor/VMM is responsible for: (A) controlling and multiplexing the underlying hardware for guests (B) writing application essays (C) replacing every device physically (D) deleting guest OSs. **Ans: A**
3. An OS running inside a VM is the: (A) guest OS (B) host hardware (C) linker (D) device buffer. **Ans: A**
4. Emulation exposes a virtual resource that may differ from: (A) the underlying physical resource (B) the file name only (C) the user’s password only (D) the scheduler queue. **Ans: A**
5. Server consolidation means: (A) running workloads previously on several machines on fewer physical machines, often as VMs (B) deleting all servers (C) removing isolation (D) replacing RAM with files. **Ans: A**

### MCQ — Medium

6. A Java VM mainly presents: (A) a virtual bytecode execution environment (B) a physical disk head (C) a semaphore queue (D) a process state only. **Ans: A**
7. A host OS runs: (A) directly on hardware in the host-based terminology (B) only inside a guest (C) only on a disk image (D) after all guests terminate. **Ans: A**
8. Virtualization is useful for cloud multi-tenancy because it provides: (A) isolation and flexible provisioning between users (B) one shared address space with no protection (C) no resource accounting (D) no scheduling. **Ans: A**
9. A RAM disk is an example of: (A) emulating storage using DRAM (B) emulating CPU using a disk only (C) deadlock detection (D) file indexing. **Ans: A**
10. A VMM must remain in control to: (A) enforce isolation and mediate privileged hardware operations (B) allow a guest to overwrite all guests (C) remove protection (D) avoid all context switches. **Ans: A**

### MCQ — Hard

11. Virtualization can incur overhead because: (A) guest operations may require mediation, translation or scheduling by the VMM (B) hardware disappears (C) all instructions are deleted (D) guests cannot execute. **Ans: A**
12. A virtual NIC is: (A) an emulated/virtual interface presented to a guest, backed by physical networking (B) necessarily a second physical cable (C) a page table (D) a CPU burst. **Ans: A**
13. A VM snapshot is useful because it: (A) captures recoverable VM state at a point in time (B) guarantees no future bugs (C) replaces the hypervisor (D) removes isolation. **Ans: A**
14. Dynamic binary translation can help an emulator by: (A) translating guest instructions into host instructions (B) translating filenames into PIDs (C) allocating semaphores (D) scheduling disks only. **Ans: A**
15. A key distinction between emulation and ordinary virtualization is that emulation may: (A) present a different architecture/resource model than the physical one (B) require identical guest and host instruction sets always (C) forbid isolation (D) eliminate software. **Ans: A**

### MCQ — Baka

16. A cloud operator wants strong tenant isolation, oversubscription and migration between x86 hosts, but a guest expects a different CPU architecture. Which combination is most appropriate? (A) VM isolation/resource scheduling plus emulation or translation for the architecture mismatch, accepting performance cost (B) FCFS scheduling only (C) a shared kernel with no isolation (D) a RAM disk only. **Ans: A**

### Open-ended

- **Easy:** Define host OS, guest OS and hypervisor. **Key:** host directly manages hardware in host-based model; guest runs within VM; hypervisor/VMM controls and isolates virtual machines.
- **Medium:** Explain three reasons organisations use VMs. **Key:** compatibility, server consolidation, isolation/multi-tenancy, easy provisioning, cloud foundation, snapshots/migration.
- **Hard:** Compare virtualization and emulation. **Key:** virtualization usually leverages same/similar hardware and aims for near-native execution; emulation models a different resource/architecture through software; emulation broader but slower.
- **Baka:** Design a VM platform for two mutually untrusted tenants with bursty CPU and storage workloads. **Key:** CPU/memory/device virtualisation; quotas and scheduling; isolation/protection; virtual networking/storage; noisy-neighbour control; snapshots/migration; overhead and threat assumptions.

## 8. Memory organization

### MCQ — Easy

1. The process image normally contains text/code, data, heap and: (A) stack (B) directory only (C) semaphore only (D) disk head. **Ans: A**
2. The linker primarily: (A) combines object modules and resolves references (B) schedules CPU bursts (C) handles page faults (D) locks a mutex. **Ans: A**
3. Compile-time binding assumes: (A) the memory location is known in advance (B) the process moves every instruction (C) no addresses exist (D) all code is virtual. **Ans: A**
4. External fragmentation means: (A) free memory exists but is split into separated holes (B) a file is too long (C) a page is invalid (D) CPU is idle. **Ans: A**
5. Paging divides logical memory into pages and physical memory into: (A) frames (B) files (C) queues (D) sectors only. **Ans: A**

### MCQ — Medium

6. Load-time binding uses: (A) relocatable code and binds addresses when loading (B) only absolute addresses fixed at compilation (C) no loader (D) page replacement. **Ans: A**
7. Execution-time binding permits a process to: (A) be moved during execution, with run-time address translation (B) avoid protection (C) use no base register (D) remove the MMU. **Ans: A**
8. With base and limit registers, a generated address is valid if it is: (A) ≥ base and < base+limit (B) equal to limit (C) less than base (D) any value. **Ans: A**
9. Fixed partitioning can suffer from: (A) internal fragmentation (B) no allocation at all (C) no protection (D) only deadlock. **Ans: A**
10. Paging removes external fragmentation mainly because: (A) pages can occupy any free frame (B) all memory becomes contiguous (C) page size is zero (D) it disables allocation. **Ans: A**

### MCQ — Hard

11. A 16-bit logical address with 4 KB pages has: (A) 4-bit offset and 12-bit page number (B) 12-bit offset and 4-bit page number (C) 16-bit offset (D) no page number. **Ans: A**
12. A page table maps: (A) logical page numbers to physical frame numbers (B) files to extensions (C) PIDs to priorities only (D) CPU bursts to deadlines. **Ans: A**
13. A two-level page table is useful mainly because it: (A) avoids allocating page-table space for unused portions of a sparse address space (B) removes all translation cost (C) prevents page faults (D) stores file attributes. **Ans: A**
14. Segmentation reflects: (A) logical variable-sized units such as code, data and stack with protection per segment (B) fixed-size pages only (C) no logical structure (D) disk scheduling. **Ans: A**
15. Internal fragmentation in paging occurs because: (A) the last allocated page may not be completely filled (B) holes exist between frames (C) the process cannot be protected (D) pages are variable-sized. **Ans: A**

### MCQ — Baka

16. A process generates logical address 2300, base=1000, limit=1500. Under base/limit relocation, which is correct? (A) valid; physical address 3300 (B) invalid because 2300≥limit (C) valid; physical address 2300 (D) invalid because physical address exceeds base. **Ans: A**

### Open-ended

- **Easy:** Describe the roles of compiler, linker and loader. **Key:** compiler source→object; linker combines objects/libraries and resolves references; loader creates image, allocates memory and loads it.
- **Medium:** Compare compile-time, load-time and execution-time address binding. **Key:** when binding occurs; absolute vs relocatable code; whether process may move during execution; hardware/OS support.
- **Hard:** Explain how paging translates a logical address and compare paging’s internal fragmentation with contiguous allocation’s external fragmentation. **Key:** split page number/offset; page table gives frame; concatenate frame+offset; fixed pages/frames reduce external holes but may waste last page.
- **Baka:** For a given address width, page size and process size, derive page-number/offset bits, page-table size, maximum internal waste and a sample physical address translation. **Key:** powers of two; entries/pages; valid frame mapping; offset unchanged; identify assumptions such as PTE size.

## 9. Virtual memory and page replacement

### MCQ — Easy

1. Virtual memory allows: (A) a logical address space larger than physical memory (B) no address translation (C) all processes to share every page (D) no disk use ever. **Ans: A**
2. Demand paging loads a page: (A) when it is referenced and not resident (B) only at shutdown (C) before the program is written (D) never. **Ans: A**
3. A page fault occurs when the page-table valid/invalid bit indicates the page is: (A) not in memory (B) definitely dirty only (C) in a free frame (D) executable. **Ans: A**
4. FIFO replacement removes the page that: (A) has been in memory the longest (B) was used most recently (C) has the smallest PID (D) is dirty always. **Ans: A**
5. Thrashing is associated with: (A) excessive page faults and little useful execution (B) no memory references (C) zero disk traffic (D) perfect locality. **Ans: A**

### MCQ — Medium

6. When a page fault occurs, the OS must first: (A) trap, save state and locate/load the requested page (B) terminate every process (C) rewrite the source code (D) ignore the reference. **Ans: A**
7. The Optimal page-replacement algorithm replaces the page whose next use is: (A) farthest in the future (B) soonest (C) never considered (D) oldest by arrival. **Ans: A**
8. LRU replaces the page that: (A) has not been used for the longest time in the past (B) entered first always (C) has the largest offset (D) is always clean. **Ans: A**
9. A dirty victim page must generally be: (A) written back before its frame is reused (B) discarded without write (C) promoted to kernel mode (D) made a semaphore. **Ans: A**
10. Global replacement allows a process to take frames from: (A) other processes’ allocations (B) only its own fixed set (C) the file directory (D) the CPU scheduler. **Ans: A**

### MCQ — Hard

11. For reference string 1,2,3,1 with 3 frames initially empty, FIFO causes: (A) 3 page faults (B) 1 (C) 4 (D) 0. **Ans: A**
12. Belady’s anomaly is associated classically with: (A) FIFO sometimes having more faults with more frames (B) Optimal always worsening (C) LRU requiring future knowledge (D) demand paging having no faults. **Ans: A**
13. The effective access time is dominated by page-fault cost when: (A) the fault probability is even small because disk I/O is vastly slower than memory (B) memory is slower than disk (C) p=0 only (D) no page is referenced. **Ans: A**
14. The working-set model estimates: (A) the pages actively used in a recent reference window (B) all files in a directory (C) CPU priority only (D) disk cylinders. **Ans: A**
15. Local replacement can prevent one process from: (A) taking frames directly from another process (B) ever faulting (C) using its own page table (D) being scheduled. **Ans: A**

### MCQ — Baka

16. With three frames and reference string 1,2,3,4,1,2,5,1,2,3,4,5, which statement is safest without calculating every algorithm? (A) FIFO and LRU may differ because recency and age order diverge; Optimal is a lower-bound comparator requiring future references (B) all algorithms must produce identical faults (C) FIFO is always optimal (D) LRU uses future knowledge. **Ans: A**

### Open-ended

- **Easy:** Trace the steps of a page fault. **Key:** detect invalid PTE; trap to OS; find free frame or victim; read page from backing store; update PTE; restart interrupted instruction.
- **Medium:** Compare FIFO, Optimal and LRU. **Key:** selection rule; Optimal theoretical minimum but needs future; FIFO simple but anomaly; LRU uses past recency and approximations.
- **Hard:** Explain thrashing and two controls for it. **Key:** too few frames/poor locality causes high fault rate and low CPU use; working-set or page-fault-frequency control; adjust degree of multiprogramming/frame allocation.
- **Baka:** Given a reference string and frame count, produce FIFO, LRU and Optimal frame tables, count faults, and explain any anomaly or tie-breaking assumption. **Key:** correct table; explicit initial state; victim rule; fault counts; identify why results differ.

## 10. File systems and disk-space allocation

### MCQ — Easy

1. The logical file system manages: (A) directories, file creation, access and protection (B) CPU burst prediction only (C) page replacement only (D) interrupts only. **Ans: A**
2. Sequential access processes bytes: (A) in order from the beginning (B) at arbitrary positions only (C) from the last directory entry (D) by page fault. **Ans: A**
3. Direct access permits: (A) reading bytes in any order using a byte number/position (B) only beginning-to-end reads (C) no writes (D) no file pointer. **Ans: A**
4. A directory entry commonly stores a file name and: (A) attributes or a pointer to file-control information (B) CPU quantum only (C) semaphore value only (D) page fault count only. **Ans: A**
5. An inode is associated with: (A) indexed allocation and file metadata/block pointers (B) CPU scheduling (C) real-time deadlines only (D) a user thread. **Ans: A**

### MCQ — Medium

6. Contiguous allocation gives good sequential access but can suffer from: (A) external fragmentation and difficult file growth (B) no locality (C) no file protection (D) no disk use. **Ans: A**
7. Linked allocation avoids external fragmentation but: (A) random/direct access is slow because pointers must be followed (B) requires one contiguous extent (C) cannot grow (D) has no pointers. **Ans: A**
8. FAT improves linked allocation lookup by: (A) placing block-link information in a table (B) removing all links (C) using CPU registers (D) storing only file names. **Ans: A**
9. An absolute path starts at: (A) the root directory (B) the current directory (C) the last opened file (D) the disk cache. **Ans: A**
10. A symbolic link usually stores: (A) a path name to the target (B) a duplicate of all file data (C) a CPU register set (D) a page frame. **Ans: A**

### MCQ — Hard

11. If the current directory is `/spell/mail`, the relative path to `/spell/mail/prt/first` is: (A) `prt/first` (B) `/spell/mail/prt/first` only (C) `first/prt` (D) `../prt/first`. **Ans: A**
12. A hard link differs from a symbolic link because a hard link: (A) refers to the file’s underlying metadata/data rather than storing a path string (B) always crosses file systems (C) is always slower (D) requires the target path to remain valid. **Ans: A**
13. In indexed allocation, a file’s index block contains: (A) pointers to its data blocks (B) all CPU registers (C) only the file extension (D) process priorities. **Ans: A**
14. A hash-table directory can be faster than a linear list but must handle: (A) collisions when names hash to the same location (B) page faults only (C) CPU preemption only (D) deadlock conditions. **Ans: A**
15. A larger allocation block tends to: (A) reduce metadata/lookup overhead but increase internal waste for small files (B) eliminate all waste and overhead (C) prevent file growth (D) remove protection. **Ans: A**

### MCQ — Baka

16. A workload contains huge sequential files plus many small files with frequent random reads and growth. Which allocation strategy is the best reasoned choice? (A) use an indexed/inode-based design, possibly with extents or direct pointers for locality, because it balances growth and random access better than pure linked allocation (B) pure linked allocation for all files (C) one enormous contiguous region for every file (D) no allocation metadata. **Ans: A**

### Open-ended

- **Easy:** Describe the main file-system layers from logical file system down to I/O control. **Key:** logical file system; file-organisation module; basic file system; I/O control/device drivers and interrupt handlers.
- **Medium:** Compare contiguous, linked and indexed allocation. **Key:** layout; sequential/direct access; fragmentation; growth; metadata overhead; FAT/inode relationship.
- **Hard:** Explain what happens internally during open, read, write and close. **Key:** directory lookup and open-file table; current-position pointer; disk location; read/write through pointer; close updates persistent directory/metadata.
- **Baka:** Design a file-system layout for a mixed workload and justify block size, free-space tracking, allocation method, directory structure and links. **Key:** workload-driven trade-offs; locality/random access; growth/fragmentation; bitmap/free list; hash/tree/linear directory choice; protection and link semantics; crash/recovery consideration.

## Rapid revision checklist

- Process state, PCB, context switch, process tree, `fork`/`wait`/IPC, user vs kernel threads.
- FCFS convoy effect; SJF/SRTF; RR quantum; priority scheduling; waiting/turnaround/response calculations.
- Race conditions; critical-section requirements; mutex/semaphore/monitor; bounded-buffer ordering.
- Coffman conditions; safe state and Banker’s algorithm; prevention vs avoidance vs detection/recovery.
- Hard vs soft real time; WCET/deadlines; priority inversion.
- Host/guest/hypervisor; emulation vs virtualisation; isolation and multi-tenancy.
- Binding stages; base/limit; fragmentation; page-table translation; segmentation.
- Demand paging; page-fault path; FIFO/Optimal/LRU; frame allocation; thrashing.
- File-system layers; access methods; directories/paths/links; contiguous/linked/indexed allocation.
