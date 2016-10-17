/* Includes */
#include <stdio.h>
#include <stdlib.h>
#include "processor.h"
#include "decode.h"
#include "ram.h"
#include "rom.h"    
#include <unistd.h>

/* Main */
int main () {
    
    /* Variable declarations. 
    You may declare others, but these were all I needed. */
    bool *ng, *zr;
    int result, ndx;
    int16 flags;
    int16 pc;
    int16 AReg, DReg;
  
  
    /* Allocate space for the ng and zr. */
    ng = (bool *)malloc(sizeof(bool));
    zr = (bool *)malloc(sizeof(bool));
  
  
    /* Zero RAM. */
    init_ram();


    /* Set the program counter to the start of ROM. */  
    pc = 0;
  

    /* As long as the pc is within the range of the size of ROM
    we should be looping. We will always engage in the same 
    thing: fetch an instruction and execute it. */
    while (pc < ROMSIZE) {
        int16 ibit, abit, cbits, dbits, jbits;
        int16 result;
        int16 AorM;
        int16 the_instruction = ROM[pc];
         
        sleep(1);
         
        /************
         * Right here is a great place for a really pretty
         * set of print statements that show you the values of 
         * the AReg, DReg, the first 8 spaces in RAM, the PC, and
         * anything else you think that will help you understand
         * what your processor is doing.
         */
        printf("------------------------------------------");
        printf("AReg:  %i \n", AReg); // AReg
        printf("------------------------------------------");
        printf("DReg:  %i", DReg); // DReg
        printf("------------------------------------------");
        printf("RAM:   "); // RAM
        show_ram(0, 8);
        printf("------------------------------------------");    
        printf("PC:    %d", pc); // PC
        printf("------------------------------------------");      
      
      
      
     
         /* If the instruction we are given is a number, we should load
        the AReg. Otherwise, we need to decode it.*/
        printf("----------------Assignment Bits----------------");
        ibit = get_i_bit(the_instruction);
        //printf("instruction type bit: %i \n, ibit");
        printf("The i-bit codes the instruction type, which is 0 for \n\
        an A-instruction and 1 for a Cinstruction.");
      
        /* The "instruction" is actually a number. 
        If that is the case, we need to load the AReg with that
        value, so we can use it in later computations. */
        if (ibit == 0) {
            AReg = the_instruction;
            pc = pc + 1;
        }
      
        /* The "instruction" is something we have to decode... 
        and, after decoding, we have to decide what to do.
        From Nand2Tetris regarding bits:
        In case of a C-instruction, the a-bit and the c-bits code the comp part,
        the d-bits code the dest part, and the j-bits code the jump part of 
        the instruction. In case of an A-instruction, the 15 bits other
        than the i-bit should be interpreted as a 15-bit constant. */
        if (ibit == 1) {
            abit  = get_a_bit(the_instruction); //instruction to go to Ram or Register
            //printf("abit value: %i \n, abit");
            
            cbits = get_c_bits(the_instruction);
            //printf("cbit values: %i \n, cbits");
            
            dbits = get_d_bits(the_instruction);
            //printf("dest bit values: %i \n, dbits");
            
            jbits = get_j_bits(the_instruction);
            //printf("jump bit values: %i \n, cbits") ; 
            printf("In case of a C-instruction, the a-bit and the c-bits \n\
            code the comp part, the d-bits code the dest part, and the j-bits \n\
            code the jump part of the instruction. In case of an A-instruction, \n\
            the 15 bits other than the i-bit should be interpreted as a 15-bit \n\
            constant.");
            
            
            /* The ALU takes two inputs. The "x" input is always
             * the DReg. The "y" input might be the AReg, or it 
             * might be from RAM. This is determined by the abit.
             */
            printf("----------------Assignment Bits----------------");
            if (abit == 0) {
                printf("abit is 0");
                AorM = AReg; 
            } 
            else {
                printf("abit is not 0");
                AorM = get_ram(AReg);
            }

            /* The ALU operates on x, y, and does some
            computation based on the cbits. You will need
             * to update your ALU so that it takes an int16 for its 
             * flags instead of an array of booleans. 
             */
            result = alu(DReg, AorM, cbits, zr, ng);
            //printf("Result is: %i \n, result");
            printf("------------------------------------------------");
            
            
            /* Now, the destination bits decide where the "result"
             * from the ALU will be stored.
             */
            printf("----------------Destination Bits----------------");
            if (dbits == 0){
                printf("dbit is 0");
                // nothing happens if dbits are 0
            }
            else if (dbits == 1){
                printf("dbit is 1");
                set_ram(AReg, result);
                // result stored in Ram if dbits are 1
            }
            else if (dbits == 2){
                printf("dbit is 2");
                DReg = result;
                // result stored in D-register if dbits are 2
            }
            else if (dbits == 3){
                printf("dbit is 3");
                set_ram(AReg, result);
                // result stored in RAM            
                DReg = result;
                // D-register is set to A-register
            } 
            else if (dbits == 4){
                printf("dbit is 4");
                AReg = result;
                // result is stored in A-register
            }
            else if (dbits == 5){
                printf("dbit is 5");
                AReg = result;
                // Result is stored in the A-register
                set_ram(AReg, result);
                // Result is ALSO stored in RAM
            }
            else if (dbits == 6){
                printf("dbit is 6");
                AReg = result;
                // Result is stored in the A-register
                DReg = result;
                // Result is ALSO stored in the D-register
            }        
            else if (dbits == 7){
                printf("dbit is 7");
                AReg = result;
                // Result is stored in the A-register
                DReg = result;
                // Result is ALSO stored in the D-register
                set_ram(AReg, result);
                // Result is ALSO stored in RAM
            }  
            else{
                printf("dbit error");
            }
            printf("------------------------------------------------");
             
             
            /* Finally, the jump bits decide what value we will
            assign to the PC next. We also need to use the zr and 
            ng values from the ALU in making that decision. */
            // FIXME: Update the PC.
            printf("------------Jump Bits/Program Counter------------");
            if (jbits == 0){
                printf("jbits are 0");
                pc += 1;
            }
            else if (jbits == 1){
                printf("jbits are 1");
                if (*ng == false || *zr == false)/*logical or*/{
                    // if jbits are 1 and result is > 0
                    pc = AReg;
                    // PC goes to A-register's value
                }
    
            }
            else if (jbits == 2){
                printf("jbits are 2");
                if (*zr == true){
                    // if jbits are 2 and result is 0
                    pc = AReg;
                    // PC goes to A-register's value
                }
    
            }
            else if (jbits == 3){
                printf("jbits are 3");
                if (*ng == false){
                    // if jbits are 3 and result is >= 0
                    pc = AReg;
                    // PC goes to A-register's value
                }
    
            } 
            else if (jbits == 4){
                printf("jbits are 4");
                if (*ng == true){
                    //if jbits are 4 and result is negative
                    pc = AReg;
                    // PC goes to A-register's value
                }
            }
            else if (jbits == 5){
                printf("jbits are 5");
                if (*zr == false){
                    //if jbits are 5 and result is not 0
                    pc = AReg;
                    // PC goes to A-register's value
                }
            }
            else if (jbits == 6){
                printf("jbit are 6");
                if (*ng == true || *zr == true){
                    // if jbits are 6 and result is <= 0
                    pc = AReg;
                    // PC goes to A-register's value
                }
            }        
            else if (jbits == 7){
                printf("jbit are 7");
                pc = AReg;
                // PC goes to A-register's value
            }  
            printf("------------------------------------------------");
        }//if statement ends
    } //while loop ends
    printf("end of while loop");
    
    /* We should never get here */
    printf("ERROR: PC value %i out of range of ROM (size: %i)\n", pc, ROMSIZE);
    return 0;
}// main ends
  