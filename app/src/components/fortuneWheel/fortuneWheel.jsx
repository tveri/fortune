import React, { useEffect, useState } from 'react'
import cl from './fortuneWheel.module.css'

export default function FortuneWheel({playerList, playerCount,  center, radius, winnerIndex}) {
  const calcCordX = (index) => {
    return center[0] + radius * Math.cos(Math.PI * (360 / playerCount) * index / 180)
  }

  const calcCordY = (index) => {
    return center[1] + radius * Math.sin(Math.PI * (360 / playerCount) * index / 180)
  }

  return (
    <div className={cl.wheelContainer}>
      <svg style={{transform: `rotate(${winnerIndex * (360 / playerCount) - (180 / playerCount)}deg)`}} className={cl.wheel} version="1.1" xmlns="http://www.w3.org/2000/svg">
        <defs>
          {playerList.map((player, index) => {
            return (
              <path id={`textpath${index}`} fill='none' d={`M${calcCordX(index+0.5)},${calcCordY(index+0.5)} L300,300`} key={index + 'htr'}/>
            )
          })}
        </defs>
        
        {playerList.map((player, index) => {
        return (
          <g key={index + 'kyug'}>
            <path d={`M300,300 L${calcCordX(index)},${calcCordY(index)} A${radius},${radius} 1 0,1 ${calcCordX(index+1)},${calcCordY(index+1)} L300,300 z`}></path>
            <g>
              <use href={`#textpath${index}`} />
              <text x={10}>
                <textPath href={`#textpath${index}`}>
                  {player.full_name}
                </textPath>
              </text>
            </g>
          </g>
        )
        })}
        
      </svg>
    </div>
  )
}