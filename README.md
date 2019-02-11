# wireless-network-power-allocatioon
multi-attenas transmission and multi channel power allocation analysis using python

Three problems have been chosen from the whole:

problem 2: 
   You have two sets of links (T1-R1 and T2-R2), with the gains given as follows: g11 =0.2,g22 =0.9,g12 =0.2,g21 =0.2. Letθ=2,N =1mW.Isitpossibleforbothlinks to be operated simultaneously? If so, what is the minimum power solution? Sketch a labeled plot of the various operating regions of transmit powers for both links (i.e. a plot where the axes are P1 and P2 and you show the conditions under which either link can receive, and if possible, also the condition under which both links can receive). Repeat the above plot for when θ = 1 and comment on how that affects the operating regions and why.

problem 3: 
  Say the vector of ratios of noise to gain Ni/gi for a set of five parallel channels is given as [3, 6, 1, 9, 5] in some suitably normalized units. Plot the optimal power allocated to each channel by water filling for sum-rate maximization, as the total power is varied.

problem 4: 
   Imagine there are two radio links (T1-R1 and T2-R2) with the following gains: g11 = 0.7, g22 = 0.4, g12 = 0.4, g21 = 0.1. Let θ = 2 and N = 1 mW.

(a) Determine the optimal power solution for this system of radios.

(b) Use the distributed Foschini-Miljanic algorithm to derive a feasible power solution. Does the algorithm give you the same answer as part (a)?
  Recall that the power update equation for the Foschini-Miljanic algorithm is as follows: 
                                                    PL(t + 1) = θ PL(t)
SINRL (t) where PL and SINRL are the power allocated and the SINR for link L, respectively. θ is the minimum required SINR for operation and t represents time. You may initialize PL(0) to 1 mW.

(c) Draw a plot showing the operating regions for both links, with P1 on the y-axis and P2 on the x-axis. On this same plot show the power allocation chosen for each iteration of the Foschini-Miljanic algorithm. Also draw a plot showing the power allocated for each link vs. time.

(d) Is it a good idea to start with an initial power allocation of 0 mW for both links?

(e) Instead of PL(0) = 1 mW, start the algorithm with different initial values. In particular, initialize P1(0) to 5 mW below and P2(0) to 5 mW above your answers from part (a). Does the algorithm still converge to the same answer from part (b)? Redraw the plots from part (c) with these new initial values.
