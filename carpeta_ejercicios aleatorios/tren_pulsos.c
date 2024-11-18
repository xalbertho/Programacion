#include <stdio.h>
#define F_CPU 8000000UL
#include <avr/io.h>
#include <util/delay.h>


int main(void){
    DDRD |=(1<<PIND0) | (1<<PIND1) |(1<<PIND2) |(1<<PIND3) |(1<<PIND5) |(1<<PIND6) |(1<<PIND7) ;

    DDRB&=(0<<PINB0);
    
    int push ;
    push=PINB & 0b00000001;

    while(1)
    {
        push= PINB & 0b00000001;
        if (push==1){
            for (int i=0; i<255; i++){
                PORTD=contador;
                _delay_ms(100);
            }
            _delay_ms(1500);
            PORTD= 0x00;
        }
    }
}

10
9
9
10
8
9