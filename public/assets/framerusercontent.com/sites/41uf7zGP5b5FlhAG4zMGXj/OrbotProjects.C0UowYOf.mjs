import{t as e}from"./rolldown-runtime.Dh6celcD.mjs";import{c as t,l as n,o as r}from"./react.CWOg5Z1e.mjs";import{Z as i,j as a,o}from"./framer.swnVdyjx.mjs";function s(e,t){let n=`
    <svg xmlns="http://www.w3.org/2000/svg" width="240" height="240" viewBox="0 0 240 240">
        <filter id="n">
            <feTurbulence
                type="fractalNoise"
                baseFrequency="${.85/Math.max(.2,t)}"
                numOctaves="3"
                stitchTiles="stitch"
            />
        </filter>
        <rect width="100%" height="100%" filter="url(#n)" opacity="${e}" />
    </svg>`;return`url("data:image/svg+xml;utf8,${encodeURIComponent(n)}")`}function c(e){let{background:r,grainOpacity:i,grainScale:a,lightColor:o,lightCoreOpacity:c,lightBloomOpacity:l,lightWashOpacity:u,lightCoreWidth:d,lightCoreBlur:f,lightBloomSize:p,lightWashWidth:m,lightWashBlur:h,topGlowOpacity:g,vignetteOpacity:_,radius:v,style:y}=e,b=s(i,a),x=s(i*.45,a*1.5);return n(`div`,{style:{...y,position:`relative`,width:`100%`,height:`100%`,overflow:`hidden`,borderRadius:v,background:r},children:[t(`div`,{style:{position:`absolute`,inset:0,background:`
                        linear-gradient(
                            180deg,
                            rgba(255,255,255,0.012) 0%,
                            rgba(255,255,255,0.006) 18%,
                            rgba(0,0,0,0.06) 100%
                        )
                    `}}),t(`div`,{style:{position:`absolute`,left:`50%`,top:`-20%`,width:`60%`,height:`55%`,transform:`translateX(-50%)`,borderRadius:`50%`,background:`radial-gradient(
                        ellipse at center,
                        ${o} 0%,
                        rgba(255,255,255,0.05) 22%,
                        transparent 72%
                    )`,filter:`blur(40px)`,opacity:g,mixBlendMode:`screen`}}),t(`div`,{style:{position:`absolute`,left:`50%`,top:`-10%`,bottom:`-8%`,width:m,transform:`translateX(-50%)`,borderRadius:999,background:`linear-gradient(
                        180deg,
                        rgba(255,255,255,0.18) 0%,
                        ${o} 16%,
                        rgba(255,255,255,0.05) 38%,
                        rgba(255,255,255,0.015) 58%,
                        transparent 100%
                    )`,filter:`blur(${h}px)`,opacity:u,mixBlendMode:`screen`}}),t(`div`,{style:{position:`absolute`,left:`50%`,top:`42%`,width:p,height:p*.72,transform:`translate(-50%, -50%)`,borderRadius:`50%`,background:`radial-gradient(
                        ellipse at center,
                        rgba(255,255,255,0.24) 0%,
                        ${o} 22%,
                        rgba(255,255,255,0.05) 42%,
                        transparent 74%
                    )`,filter:`blur(48px)`,opacity:l,mixBlendMode:`screen`}}),t(`div`,{style:{position:`absolute`,left:`50%`,top:`37%`,width:d,height:`48%`,transform:`translateX(-50%)`,borderRadius:999,background:`linear-gradient(
                        180deg,
                        rgba(255,255,255,0.38) 0%,
                        rgba(255,245,230,0.22) 18%,
                        rgba(255,230,200,0.08) 42%,
                        rgba(255,255,255,0.025) 70%,
                        transparent 100%
                    )`,filter:`blur(${f}px)`,opacity:c,mixBlendMode:`screen`}}),t(`div`,{style:{position:`absolute`,inset:`-10%`,backgroundImage:b,backgroundRepeat:`repeat`,backgroundSize:`${120*a}px ${120*a}px`,mixBlendMode:`soft-light`,opacity:1}}),t(`div`,{style:{position:`absolute`,inset:`-10%`,backgroundImage:x,backgroundRepeat:`repeat`,backgroundSize:`${180*a}px ${180*a}px`,mixBlendMode:`overlay`,opacity:.65}}),t(`div`,{style:{position:`absolute`,inset:0,background:`
                        radial-gradient(
                            ellipse at center,
                            transparent 0%,
                            rgba(0,0,0,0.06) 72%,
                            rgba(0,0,0,0.16) 100%
                        )
                    `}}),t(`div`,{style:{position:`absolute`,inset:0,background:`radial-gradient(
                        ellipse at center,
                        transparent 36%,
                        rgba(0,0,0,${_*.32}) 72%,
                        rgba(0,0,0,${_}) 100%
                    )`}})]})}var l=e((()=>{r(),i(),c.defaultProps={background:`#0B0908`,grainOpacity:.16,grainScale:1,lightColor:`rgba(225,170,110,0.28)`,lightCoreOpacity:.42,lightBloomOpacity:.34,lightWashOpacity:.22,lightCoreWidth:120,lightCoreBlur:26,lightBloomSize:680,lightWashWidth:300,lightWashBlur:52,topGlowOpacity:.22,vignetteOpacity:.58,radius:0},a(c,{background:{type:o.Color,title:`Background`},grainOpacity:{type:o.Number,title:`Grain opacity`,min:0,max:1,step:.01},grainScale:{type:o.Number,title:`Grain scale`,min:.5,max:3,step:.1},lightColor:{type:o.Color,title:`Light color`},lightCoreOpacity:{type:o.Number,title:`Core opacity`,min:0,max:1,step:.01},lightBloomOpacity:{type:o.Number,title:`Bloom opacity`,min:0,max:1,step:.01},lightWashOpacity:{type:o.Number,title:`Wash opacity`,min:0,max:1,step:.01},lightCoreWidth:{type:o.Number,title:`Core width`,min:20,max:400,step:1,unit:`px`},lightCoreBlur:{type:o.Number,title:`Core blur`,min:0,max:120,step:1,unit:`px`},lightBloomSize:{type:o.Number,title:`Bloom size`,min:100,max:1400,step:1,unit:`px`},lightWashWidth:{type:o.Number,title:`Wash width`,min:40,max:700,step:1,unit:`px`},lightWashBlur:{type:o.Number,title:`Wash blur`,min:0,max:160,step:1,unit:`px`},topGlowOpacity:{type:o.Number,title:`Top glow`,min:0,max:1,step:.01},vignetteOpacity:{type:o.Number,title:`Vignette`,min:0,max:1,step:.01},radius:{type:o.Number,title:`Radius`,min:0,max:80,step:1,unit:`px`}})}));export{l as n,c as t};
//# sourceMappingURL=OrbotProjects.C0UowYOf.mjs.map