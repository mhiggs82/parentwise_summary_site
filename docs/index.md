---
hide:
  - navigation
  - toc
---

<div class="font-inter text-slate-800 bg-slate-50 -mx-4 sm:-mx-6 lg:-mx-8">

    <!-- Hero Section -->
    <main class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 pt-16 pb-20">
        
        <!-- Headlines -->
        <div class="max-w-4xl">
            <h1 class="text-4xl lg:text-5xl font-semibold text-slate-900 tracking-tight leading-[1.15] mb-6">
                Search for parenting wisdom, proven strategies, and expert authors.
            </h1>
            <p class="text-xl text-slate-500 font-normal leading-relaxed max-w-2xl mb-10">
                Search through our 240+ book summaries, compare approaches, and find the best fit for your family dynamics.
            </p>
        </div>

        <!-- Main Search Bar -->
        <div class="flex flex-col lg:flex-row gap-2 transition-shadow duration-300 hover:shadow-[0_8px_40px_rgb(0,0,0,0.08)] bg-white border-slate-100 border rounded-xl pt-2 pr-2 pb-2 pl-2 shadow-[0_8px_30px_rgb(0,0,0,0.06)] gap-x-2 gap-y-2">

            <!-- Input 1: Keyword -->
            <div class="flex-1 group relative">
                <div class="absolute inset-y-0 left-0 pl-4 flex items-center pointer-events-none">
                    <i data-lucide="search" class="w-5 h-5 text-slate-400 group-hover:text-[#4F46E5] transition-colors"></i>
                </div>
                <input type="text" id="hero-search-input" class="block placeholder:text-slate-400 focus:ring-0 focus:bg-slate-50 transition-colors text-lg font-normal text-slate-900 bg-transparent w-full rounded-lg pt-4 pr-4 pb-4 pl-12 border-none outline-none" placeholder="Book title, Author or Topic..." onkeydown="if(event.key==='Enter') window.location.href='/search/?q=' + encodeURIComponent(this.value)">
            </div>

            <!-- Divider (Desktop) -->
            <div class="hidden lg:block w-px bg-slate-200 my-3"></div>

            <!-- Input 2: Category (Visual only allows selection but maps to search for now) -->
            <div class="flex-1 relative group">
                <div class="absolute inset-y-0 left-0 pl-4 flex items-center pointer-events-none">
                    <i data-lucide="book-open" class="w-5 h-5 text-slate-400 group-hover:text-[#4F46E5] transition-colors"></i>
                </div>
                <input type="text" class="block placeholder:text-slate-400 focus:ring-0 focus:bg-slate-50 transition-colors text-lg font-normal text-slate-900 bg-transparent w-full rounded-lg pt-4 pr-4 pb-4 pl-12 border-none outline-none" placeholder="Category (e.g. Communication, Teens)">
            </div>

            <!-- Action Button -->
            <button onclick="window.location.href='/search/?q=' + encodeURIComponent(document.getElementById('hero-search-input').value)" class="w-full lg:w-auto px-8 py-3 bg-[#4F46E5] hover:bg-[#4338ca] text-white text-lg font-medium rounded-lg transition-all duration-200 shadow-sm hover:shadow-md transform active:scale-95 flex items-center justify-center gap-2 cursor-pointer border-none">
                <span class="">Find wisdom</span>
            </button>
        </div>

        <!-- Value Props -->
        <div class="mt-20 grid grid-cols-1 md:grid-cols-3 gap-12 text-center">
            <!-- Prop 1 -->
            <div class="flex flex-col items-center group cursor-default">
                <div class="group-hover:scale-110 transition-transform duration-300 text-[#4F46E5] bg-white rounded-full mb-4 px-3 py-3 shadow-sm">
                    <i data-lucide="library" class="w-8 h-8 stroke-[1.25]"></i>
                </div>
                <h3 class="text-lg font-semibold text-slate-900 mb-2 tracking-tight">Most complete library</h3>
                <p class="text-base text-slate-500 font-normal leading-relaxed">The ParentWise database covers communication, discipline, and emotional intelligence from top experts.</p>
            </div>
            
            <!-- Prop 2 -->
            <div class="flex flex-col items-center group cursor-default">
                <div class="group-hover:scale-110 transition-transform duration-300 text-[#4F46E5] bg-white rounded-full mb-4 px-3 py-3 shadow-sm">
                    <i data-lucide="check-circle-2" class="w-8 h-8 stroke-[1.25]"></i>
                </div>
                <h3 class="text-lg font-semibold text-slate-900 mb-2 tracking-tight">Verified Strategies</h3>
                <p class="text-base text-slate-500 font-normal leading-relaxed">Browse confidently through summaries backed by psychological research and proven results.</p>
            </div>

            <!-- Prop 3 -->
            <div class="flex flex-col items-center group cursor-default">
                <div class="group-hover:scale-110 transition-transform duration-300 text-[#4F46E5] bg-white rounded-full mb-4 px-3 py-3 shadow-sm">
                    <i data-lucide="zap" class="w-8 h-8 stroke-[1.25]"></i>
                </div>
                <h3 class="text-lg font-semibold text-slate-900 mb-2 tracking-tight">Actionable Insights</h3>
                <p class="text-base text-slate-500 font-normal leading-relaxed">Get to the core implementation steps quickly. No fluff, just the tools you need to parent better.</p>
            </div>
        </div>

    </main>

    <!-- Purple Carousel Section (Featured Specs) -->
    <section class="bg-[#4F46E5] py-20 overflow-hidden relative">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 mb-10 flex flex-col md:flex-row justify-between items-end gap-6">
            <div class="">
                <span class="inline-block px-3 py-1 bg-green-400/20 text-green-100 text-sm font-medium rounded-full mb-4 border border-green-400/30">
                    Essential Reading
                </span>
                <h2 class="text-3xl lg:text-4xl font-semibold text-white tracking-tight">Foundational books for every parent</h2>
            </div>
            
            <div class="flex gap-3">
                <button class="w-10 h-10 rounded-lg bg-white/10 hover:bg-white/20 flex items-center justify-center text-white transition-colors backdrop-blur-sm border-none cursor-pointer">
                    <i data-lucide="arrow-left" class="w-5 h-5"></i>
                </button>
                <button class="w-10 h-10 rounded-lg bg-white/10 hover:bg-white/20 flex items-center justify-center text-white transition-colors backdrop-blur-sm border-none cursor-pointer">
                    <i data-lucide="arrow-right" class="w-5 h-5"></i>
                </button>
            </div>
        </div>

        <!-- Scrolling Wrapper -->
        <div class="w-full relative">
            <div class="flex w-[200%] animate-scroll hover:pause">
                <div class="flex pl-4 gap-x-6 gap-y-6">

                    <!-- Card 1 -->
                    <a href="Book_Summaries/FOUND/FOUND-001 - Good Inside by Becky Kennedy/" class="block text-decoration-none">
                    <div class="min-w-[320px] w-[320px] bg-white p-6 rounded-2xl shadow-xl transform transition-transform duration-300 hover:-translate-y-2 cursor-pointer group">
                        <div class="flex flex-col items-center text-center">
                            <div class="w-24 h-24 rounded-2xl overflow-hidden mb-4 shadow-inner bg-slate-100 flex items-center justify-center text-4xl">
                                📚
                            </div>
                            <h3 class="text-xl font-semibold text-slate-900 mb-1">Good Inside</h3>
                            <p class="text-sm text-slate-500 font-medium mb-3">Dr. Becky Kennedy</p>
                            <div class="flex items-center gap-1 mb-6 justify-center">
                                <div class="flex text-green-500">
                                    <i data-lucide="star" class="w-4 h-4 fill-current"></i>
                                    <i data-lucide="star" class="w-4 h-4 fill-current"></i>
                                    <i data-lucide="star" class="w-4 h-4 fill-current"></i>
                                    <i data-lucide="star" class="w-4 h-4 fill-current"></i>
                                    <i data-lucide="star" class="w-4 h-4 fill-current"></i>
                                </div>
                                <span class="text-xs font-semibold text-slate-900 ml-1">Must Read</span>
                            </div>
                            <div class="w-full pt-4 border-t border-slate-100 text-left">
                                <p class="text-xs font-semibold text-slate-400 uppercase tracking-wider mb-2">Key Topics</p>
                                <p class="text-xs text-slate-500 font-normal leading-relaxed line-clamp-3">
                                    Internal family systems, resilience, boundaries, connection first.
                                </p>
                            </div>
                        </div>
                    </div>
                    </a>

                    <!-- Card 2 -->
                    <a href="Book_Summaries/COMM/COMM-002 - How to Talk So Kids Will Listen and Listen So Kids Will Talk by Adele Faber and Elaine Mazlish/" class="block text-decoration-none">
                    <div class="min-w-[320px] w-[320px] bg-white p-6 rounded-2xl shadow-xl transform transition-transform duration-300 hover:-translate-y-2 cursor-pointer group">
                        <div class="flex flex-col items-center text-center">
                            <div class="w-24 h-24 rounded-2xl overflow-hidden mb-4 shadow-inner bg-slate-100 flex items-center justify-center text-4xl">
                                🗣️
                            </div>
                            <h3 class="text-xl font-semibold text-slate-900 mb-1">How to Talk...</h3>
                            <p class="text-sm text-slate-500 font-medium mb-3">Faber & Mazlish</p>
                            <div class="flex items-center gap-1 mb-6 justify-center">
                                <div class="flex text-green-500">
                                    <i data-lucide="star" class="w-4 h-4 fill-current"></i>
                                    <i data-lucide="star" class="w-4 h-4 fill-current"></i>
                                    <i data-lucide="star" class="w-4 h-4 fill-current"></i>
                                    <i data-lucide="star" class="w-4 h-4 fill-current"></i>
                                    <i data-lucide="star" class="w-4 h-4 fill-current"></i>
                                </div>
                                <span class="text-xs font-semibold text-slate-900 ml-1">Classic</span>
                            </div>
                            <div class="w-full pt-4 border-t border-slate-100 text-left">
                                <p class="text-xs font-semibold text-slate-400 uppercase tracking-wider mb-2">Key Topics</p>
                                <p class="text-xs text-slate-500 font-normal leading-relaxed line-clamp-3">
                                    Communication, cooperation, alternatives to punishment, autonomy.
                                </p>
                            </div>
                        </div>
                    </div>
                    </a>

                    <!-- Card 3 -->
                    <a href="Book_Summaries/FOUND/FOUND-003 - The Whole-Brain Child by Daniel Siegel and Tina Payne Bryson/" class="block text-decoration-none">
                    <div class="min-w-[320px] w-[320px] bg-white p-6 rounded-2xl shadow-xl transform transition-transform duration-300 hover:-translate-y-2 cursor-pointer group">
                        <div class="flex flex-col items-center text-center">
                            <div class="w-24 h-24 rounded-2xl overflow-hidden mb-4 shadow-inner bg-slate-100 flex items-center justify-center text-4xl">
                                🧠
                            </div>
                            <h3 class="text-xl font-semibold text-slate-900 mb-1">The Whole-Brain Child</h3>
                            <p class="text-sm text-slate-500 font-medium mb-3">Siegel & Bryson</p>
                            <div class="flex items-center gap-1 mb-6 justify-center">
                                <div class="flex text-green-500">
                                    <i data-lucide="star" class="w-4 h-4 fill-current"></i>
                                    <i data-lucide="star" class="w-4 h-4 fill-current"></i>
                                    <i data-lucide="star" class="w-4 h-4 fill-current"></i>
                                    <i data-lucide="star" class="w-4 h-4 fill-current"></i>
                                    <i data-lucide="star" class="w-4 h-4 fill-current"></i>
                                </div>
                                <span class="text-xs font-semibold text-slate-900 ml-1">Neuroscience</span>
                            </div>
                            <div class="w-full pt-4 border-t border-slate-100 text-left">
                                <p class="text-xs font-semibold text-slate-400 uppercase tracking-wider mb-2">Key Topics</p>
                                <p class="text-xs text-slate-500 font-normal leading-relaxed line-clamp-3">
                                    Integration, emotion regulation, left/right brain, upstairs/downstairs brain.
                                </p>
                            </div>
                        </div>
                    </div>
                    </a>

                     <!-- Card 4 -->
                    <a href="Book_Summaries/TEEN/TEEN-013 - The Anxious Generation by Jonathan Haidt/" class="block text-decoration-none">
                    <div class="min-w-[320px] w-[320px] bg-white p-6 rounded-2xl shadow-xl transform transition-transform duration-300 hover:-translate-y-2 cursor-pointer group">
                        <div class="flex flex-col items-center text-center">
                            <div class="w-24 h-24 rounded-2xl overflow-hidden mb-4 shadow-inner bg-slate-100 flex items-center justify-center text-4xl">
                                📱
                            </div>
                            <h3 class="text-xl font-semibold text-slate-900 mb-1">The Anxious Generation</h3>
                            <p class="text-sm text-slate-500 font-medium mb-3">Jonathan Haidt</p>
                            <div class="flex items-center gap-1 mb-6 justify-center">
                                <div class="flex text-green-500">
                                    <i data-lucide="star" class="w-4 h-4 fill-current"></i>
                                    <i data-lucide="star" class="w-4 h-4 fill-current"></i>
                                    <i data-lucide="star" class="w-4 h-4 fill-current"></i>
                                    <i data-lucide="star" class="w-4 h-4 fill-current"></i>
                                    <i data-lucide="star" class="w-4 h-4 fill-current"></i>
                                </div>
                                <span class="text-xs font-semibold text-slate-900 ml-1">New Release</span>
                            </div>
                            <div class="w-full pt-4 border-t border-slate-100 text-left">
                                <p class="text-xs font-semibold text-slate-400 uppercase tracking-wider mb-2">Key Topics</p>
                                <p class="text-xs text-slate-500 font-normal leading-relaxed line-clamp-3">
                                    Digital wellness, play-based childhood, mental health crisis, phone bans.
                                </p>
                            </div>
                        </div>
                    </div>
                    </a>

                </div>
            </div>
        </div>
    </section>

    <!-- Categories Grid Section -->
    <section class="py-24 bg-white relative overflow-hidden">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="text-center max-w-3xl mx-auto mb-20">
                <h2 class="text-4xl lg:text-5xl font-semibold text-slate-900 tracking-tight mb-6">Explore the content library</h2>
                <p class="text-xl text-slate-500 font-normal">Find summaries by topic, age group, or specific challenge.</p>
            </div>

            <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
                <!-- Card 1 -->
                <a href="Book_Summaries/COMM/" class="block text-decoration-none group">
                <div class="p-8 border border-slate-200 rounded-2xl shadow-[0_2px_8px_rgba(0,0,0,0.04)] hover:shadow-lg transition-all duration-300 bg-white h-full">
                    <div class="mb-6 text-[#4F46E5] group-hover:scale-110 transition-transform duration-300 origin-left">
                        <i data-lucide="mic" class="w-8 h-8"></i>
                    </div>
                    <h3 class="text-xl font-semibold text-slate-900 mb-4 tracking-tight">Communication</h3>
                    <p class="text-base text-slate-500 leading-relaxed font-normal">
                        Learn how to talk so kids will listen, de-escalate conflicts, and build a lasting bond through words.
                    </p>
                </div>
                </a>

                <!-- Card 2 -->
                <a href="Book_Summaries/TEEN/" class="block text-decoration-none group">
                <div class="p-8 border border-slate-200 rounded-2xl shadow-[0_2px_8px_rgba(0,0,0,0.04)] hover:shadow-lg transition-all duration-300 bg-white h-full">
                    <div class="mb-6 text-[#4F46E5] group-hover:scale-110 transition-transform duration-300 origin-left">
                        <i data-lucide="users" class="w-8 h-8"></i>
                    </div>
                    <h3 class="text-xl font-semibold text-slate-900 mb-4 tracking-tight">Teenagers</h3>
                    <p class="text-base text-slate-500 leading-relaxed font-normal">
                        Navigate the turbulent teen years with guides on anxiety, screens, autonomy, and connection.
                    </p>
                </div>
                </a>

                <!-- Card 3 -->
                <a href="Book_Summaries/MENT/" class="block text-decoration-none group">
                <div class="p-8 border border-slate-200 rounded-2xl shadow-[0_2px_8px_rgba(0,0,0,0.04)] hover:shadow-lg transition-all duration-300 bg-white h-full">
                    <div class="mb-6 text-[#4F46E5] group-hover:scale-110 transition-transform duration-300 origin-left">
                        <i data-lucide="heart-pulse" class="w-8 h-8"></i>
                    </div>
                    <h3 class="text-xl font-semibold text-slate-900 mb-4 tracking-tight">Mental Health</h3>
                    <p class="text-base text-slate-500 leading-relaxed font-normal">
                        Support your child's emotional well-being with insights on anxiety, depression, and resilience.
                    </p>
                </div>
                </a>
            </div>
        </div>
    </section>

    <!-- Specific Categories List Section (Gradient BG) -->
    <section class="py-24 bg-gradient-to-br from-[#DCD6FF] via-[#E2E8FF] to-[#C9FBEF]">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <h2 class="text-4xl font-bold text-slate-900 tracking-tight mb-12 text-center">Browse by expertise...</h2>

            <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                
                <a href="Book_Summaries/FMLY/" class="group flex items-center justify-between p-6 bg-white rounded-lg shadow-sm hover:shadow-md transition-all duration-200 border border-transparent hover:border-indigo-100 text-decoration-none">
                    <div class="flex items-start gap-5">
                        <div class="mt-0.5 text-[#6366F1]">
                            <i data-lucide="home" class="w-6 h-6"></i>
                        </div>
                        <div>
                            <h3 class="text-lg font-bold text-slate-900 !m-0">Family Dynamics</h3>
                            <p class="text-sm text-slate-500 mt-1 font-medium !m-0">Siblings, divorce, blended families</p>
                        </div>
                    </div>
                    <div class="text-[#6366F1] pl-4">
                        <i data-lucide="arrow-right" class="w-5 h-5 transform group-hover:translate-x-1 transition-transform"></i>
                    </div>
                </a>

                <a href="Book_Summaries/DIGI/" class="group flex items-center justify-between p-6 bg-white rounded-lg shadow-sm hover:shadow-md transition-all duration-200 border border-transparent hover:border-indigo-100 text-decoration-none">
                    <div class="flex items-start gap-5">
                        <div class="mt-0.5 text-[#6366F1]">
                            <i data-lucide="smartphone" class="w-6 h-6"></i>
                        </div>
                        <div>
                            <h3 class="text-lg font-bold text-slate-900 !m-0">Digital World</h3>
                            <p class="text-sm text-slate-500 mt-1 font-medium !m-0">Screen time, social media, safety</p>
                        </div>
                    </div>
                    <div class="text-[#6366F1] pl-4">
                        <i data-lucide="arrow-right" class="w-5 h-5 transform group-hover:translate-x-1 transition-transform"></i>
                    </div>
                </a>

                <a href="Book_Summaries/GNDR/" class="group flex items-center justify-between p-6 bg-white rounded-lg shadow-sm hover:shadow-md transition-all duration-200 border border-transparent hover:border-indigo-100 text-decoration-none">
                    <div class="flex items-start gap-5">
                        <div class="mt-0.5 text-[#6366F1]">
                            <i data-lucide="user" class="w-6 h-6"></i>
                        </div>
                        <div>
                            <h3 class="text-lg font-bold text-slate-900 !m-0">Identity & Gender</h3>
                            <p class="text-sm text-slate-500 mt-1 font-medium !m-0">Boys, girls, gender identity, growth</p>
                        </div>
                    </div>
                    <div class="text-[#6366F1] pl-4">
                        <i data-lucide="arrow-right" class="w-5 h-5 transform group-hover:translate-x-1 transition-transform"></i>
                    </div>
                </a>

                <a href="Book_Summaries/SPEC/" class="group flex items-center justify-between p-6 bg-white rounded-lg shadow-sm hover:shadow-md transition-all duration-200 border border-transparent hover:border-indigo-100 text-decoration-none">
                    <div class="flex items-start gap-5">
                        <div class="mt-0.5 text-[#6366F1]">
                            <i data-lucide="star" class="w-6 h-6"></i>
                        </div>
                        <div>
                            <h3 class="text-lg font-bold text-slate-900 !m-0">Special Needs (Neurodivergence)</h3>
                            <p class="text-sm text-slate-500 mt-1 font-medium !m-0">ADHD, Autism, sensory processing</p>
                        </div>
                    </div>
                    <div class="text-[#6366F1] pl-4">
                        <i data-lucide="arrow-right" class="w-5 h-5 transform group-hover:translate-x-1 transition-transform"></i>
                    </div>
                </a>
                
            </div>
        </div>
    </section>

</div>

<script>
    // Initialize Lucide Icons
    lucide.createIcons();
    
    // Simple custom scroll animation retention
    // The Tailwind classes 'animate-scroll' need keyframes.
    // Adding them via JS to ensure they work even if style tags are quirky in MD
    const style = document.createElement('style');
    style.innerHTML = `
      @keyframes scroll {
        0% { transform: translateX(0); }
        100% { transform: translateX(-50%); }
      }
      .animate-scroll {
        animation: scroll 40s linear infinite;
        width: max-content;
      }
      .animate-scroll:hover {
        animation-play-state: paused;
      }
    `;
    document.head.appendChild(style);
</script>
