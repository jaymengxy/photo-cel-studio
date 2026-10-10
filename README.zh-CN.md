# photo-cel-studio

[English](README.md) | 简体中文

**摄影瞬间 → 保真 → Cel Style Profile → Scene Mode → Atmosphere → 重绘 → 独立质量门 → 验证导出。** v0.2 默认 `mature-ova` 固定为更明显的手绘粗细变化、人物平涂与简练衣褶、克制的灰蓝背景和大面积冷色暗部、建筑/招牌/天空的绘画质感。原图决定场景关系与光线；保留身份色和局部暖光。默认交付长边 **540 像素** 的原比例 PNG，同时保留生成原尺寸文件。

这个项目是一个供 Codex 等支持 Agent Skills 的环境读取的**视觉创作 Skill**，不是图片处理算法、滤镜、LUT 或独立图像生成模型。它必须配合一个**可用的图像编辑或生成工具**，才能真正输出图片。

## Installation / 安装（Codex）

克隆到你的 Codex skills 目录：

```bash
git clone https://github.com/jaymengxy/photo-cel-studio.git ~/.codex/skills/photo-cel-studio
```

或者使用 SSH（已经配置 GitHub SSH key 时）：

```bash
git clone git@github.com:jaymengxy/photo-cel-studio.git ~/.codex/skills/photo-cel-studio
```

然后重启 / 刷新 Codex 会话，使 `SKILL.md` 被扫描。也可以在支持 `~/.agents/skills/` 的 Agent Skills 运行环境中安装相同文件夹。开发中的功能请使用项目分支的文件，正式使用时以合并到 `main` 的版本为准。

**注意：** Codex 中安装 Skill ≠ 自动安装图像生成工具。需要在当前环境配置支持参考图的图像编辑能力。若当前运行环境 **no image editing capability**，本 Skill 只能提供编辑任务书，不能声称已经生成了图像。

### v0.2 开发分支（可选）

```bash
git clone -b feat/photo-cel-studio-v0.2 git@github.com:jaymengxy/photo-cel-studio.git ~/.codex/skills/photo-cel-studio
```

`main` 已包含 v0.2，默认使用上面的安装命令即可。如需查看 v0.2 开发分支，在已克隆的 Skill 目录中执行 `git fetch origin && git switch feat/photo-cel-studio-v0.2`，再重启 / 刷新会话。开发仓库 `~/Code/photo-cel-studio` 和安装目录是不同的副本；修改开发仓库不会自动更新已安装的 Skill。

### 历史 v0.1 Draft PR 分支安装

```bash
git clone -b design/photo-cel-studio-v0.1 git@github.com:jaymengxy/photo-cel-studio.git ~/.codex/skills/photo-cel-studio
```

这个命令仅用于查看历史 v0.1。如果已克隆仓库，可执行 `git fetch origin && git switch design/photo-cel-studio-v0.1`。回到当前版本时执行 `git switch main && git pull --ff-only`。这个 Skill 需要参考图像编辑/生成能力，否则只能给出编辑任务书。

## 使用

在支持读取本 Skill 的会话中上传一张自己的照片：

```text
使用 $photo-cel-studio 将这张照片转成复古日式赛璐璐动画剧照，
保留原始人物/动物、动作、关键物品和构图。
```

更多例子：

```text
使用 $photo-cel-studio 处理这组五张扫街照片，让线条、平涂和阴影
保持系列感；允许每张图片自动匹配合适的场景模式。
```

```text
使用 $photo-cel-studio，主模式 vehicle-mechanical，
只在原图确实存在霓虹灯和潮湿路面时采用 neon-night + rainy。
```

```text
以这张我已确认的成品为 master-lock，
只修正鱼尾，保留人物、构图、颜色和光线，其他元素保持不变。
```

## 核心设计

**共享绘制语法：** 有层次的轮廓、源图导出的平涂色块、2–3 个主要明暗色阶和塑造体积的硬边阴影、可信的人体/动物/机械结构，以及绘制出来的动画背景。共享层保持年代中性，具体线条性格、配色、年代感和介质处理由 Profile 决定。输出默认**无文字、原图比例、保留镜头、适度风格化**。

**三层风格架构：**

| 维度 | 每张输出选择 | 职责 / 注册表 |
| --- | --- | --- |
| Cel Style Profile | 恰好 1 个 | 年代、线条、色彩、明暗组织、背景绘制和介质；[Profile Registry](references/cel-era-profiles.md) |
| Scene Mode | 恰好 1 个主模式；未知题材保留中性回退 | 题材的解剖、机械、建筑、动作与构图；[Mode Registry](references/scene-modes.md) |
| Atmosphere Profiles | 0–2 个兼容项 | 原片可见的光线与天气；[Atmosphere Registry](references/atmosphere-selection.md) |

**五种 Cel Style Profiles：**

| ID | 可观察的绘制差异 |
| --- | --- |
| `mature-ova`（默认） | 明显手绘线条层次、人物 base + 一块连贯阴影、少量衣褶/反光、灰蓝背景与冷色暗部、传统绘画背景；长边 540 PNG + 原尺寸文件 |
| `clean-modern-cel` | 更精确规律的线条、清晰明亮的源图色组、整洁的平涂边缘、默认无模拟颗粒；保留成熟比例 |
| `urban-noir-cel` | 冷峻的次要色组、源光支持的更强明暗对比、较重轮廓和局部暗部融合；白天仍然是白天 |
| `industrial-mecha-cel` | 机械连接、轮胎/前叉/发动机透视、负重体块和金属分面更明确；真实车辆不会变成机甲 |
| `warm-daily-ova` | 温暖克制的日常综合色、自然表情、柔和收笔和稳定硬边明暗、具有生活感的手绘环境；不会默认幼态化 |

**默认与自动的区别：** 没有指定风格时始终使用 `mature-ova`，汽车、摩托、宠物也一样。`scene_mode: auto` 只自动选择题材模式。只有明确指定 `cel_style_profile: auto`，才按 Profile Registry 的条件选择一个风格；普通车辆模式可以推荐工业对照，但不会自行替换默认风格。显式风格选择优先于自动路由。

### v0.2 单图与风格对照

默认单图：

```text
使用 $photo-cel-studio 转换这张摩托车街拍。
保持黄色上衣、黑色头盔、摩托结构和骑手/橙白货车的原始关系，
采用默认 mature-ova，保留日景，不添加雨、霓虹或新阴影。
```

明确选择现代风格：

```text
使用 $photo-cel-studio，cel_style_profile: clean-modern-cel，
主模式 vehicle-mechanical，保留原图的车辆、人物和街道结构。
```

仅在希望风格随题材自动匹配时：

```text
使用 $photo-cel-studio，cel_style_profile: auto，scene_mode: auto。
先说明最终选择的一个风格和一个主模式，再按原片光线处理。
```

同一原图的多风格对照：

```text
使用 $photo-cel-studio，将同一张摩托原图分别转换为 mature-ova、
industrial-mecha-cel、clean-modern-cel。使用相同模型/编辑后端、输入比例、
保真约束、主模式、氛围和构图，每个风格输出一张独立图片，不要拼贴。
比较线条、机械结构、平涂明暗、配色、背景和介质，并分别报告保真与风格质量。
```

每次编辑都重新引用同一原图，不将前一个风格成品作为下一个输入。对照是明确请求多个独立成品；默认单图仍然只输出一个画面。模型版本或输入设置变化时需要重新控制条件，不能把差异全部归因于 Profile。Master Lock 中只改一处的请求，仍然锁定已接受的其他区域与风格。

### v0.2 风格控制

保留 v0.1 的十个默认字段，增加以下可选控制：

| 字段 | 默认 | 意义与边界 |
| --- | --- | --- |
| `cel_style_profile` | `mature-ova` | 一个已注册 ID 或显式 `auto` |
| `profile_intensity` | `high` | 默认强化手绘与平涂；调整强度不能降低保真优先级 |
| `palette_character` | `cool-restrained` | 克制背景与暗部；保留服装、毛色、肤色、车漆与原片暖光 |
| `surface_texture` | `subtle-analog` | `none` / `subtle-analog` / `moderate-analog`；介质纹理不能替代轮廓、平涂和阴影绘制 |
| `delivery_long_edge` | `profile-default` → mature-ova 为 `540` | 显式正整数 / native 优先，其他 Profile 默认 native；保持比例、不放大、不裁切 |
| `retain_native` | `true` | 原尺寸文件与交付文件分别保存，导出不覆盖原尺寸文件 |
| `delivery_format` | `png` | 实际导出并核验尺寸，不能把提示词尺寸当作已实现 |

显式选择其他 Profile 后，未指定控制采用该 Profile 的基底：例如现代风格为 `clear-bright` 配色和 `none` 表面纹理，Noir 为 `cool-restrained`，日常风格为 `warm-restrained`。默认 preset 不是用户显式覆盖；具体允许值及冲突处理见 [Profile Registry](references/cel-era-profiles.md)。

### 固定输出方式与影响范围

完整可复用提示词、模式适配和导出步骤见 [固定绘制与导出规范](references/mature-cel-render.md)。默认 mature-ova 下全部 14 个模式继承这套绘制/输出方法；城市、车辆最直接，建筑、工业、风景、室内主要改变环境绘画组织。人物/动作/宠物/静物/食物/微距采用线稿和平涂经济性，不把皮肤、食物、毛色或暖光室内整体染蓝。建筑样式、材质、时代改变仍需用户授权。

2:3 输出 360×540，3:2 输出 540×360，方图输出 540×540；其他比例保留原比例，小于 540 的原尺寸不放大。保存 native 后再导出、核验宽高并显示交付图。macOS 生成 PNG 的导出命令：

```bash
python3 scripts/export_frame.py /absolute/native.png /absolute/delivery.png --max-edge 540
```

显式其他 Profile 保留自己的风格与原尺寸交付基底；多风格对照统一交付尺寸，避免像素密度混淆。Master Lock 保留已认可尺寸和其他区域。降低像素不能代替平涂、线稿与背景重绘，不能只套纹理或蓝色滤镜。

**14 个主要场景模式（选择 1 个）：**

| 模式 | 主要用途 |
| --- | --- |
| `urban-cinematic` | 街拍 / 城市生活 |
| `quiet-dramatic` | 安静的人物与沉思场面 |
| `dynamic-action` | 动作、跑跳、运动 |
| `youth-energetic` | 儿童互动及活泼场景 |
| `sci-fi-industrial` | 工业结构与经用户同意的未来设计 |
| `everyday-still-life` | 日常器物、小型静物、容器中的鱼 |
| `landscape-cinematic` | 山海、湖泊、自然风光 |
| `pet-character` | 宠物特写和互动 |
| `vehicle-mechanical` | 车辆、交通机械 |
| `architecture-graphic` | 建筑、楼梯、桥梁、结构细节 |
| `portrait-character` | 人像及个人特色 |
| `food-lifestyle` | 食物、咖啡、餐桌 |
| `macro-nature` | 花卉、昆虫、微距自然 |
| `interior-atmosphere` | 家居与室内空间 |

**6 个可选氛围模式（自动 0–2 个）：** `neon-night`、`golden-hour`、`rainy`、`snowy`、`misty`、`backlit`。

**自动选择尊重证据：** 真实照片里没有雨、霓虹或落日时，不会自动捏造这些条件。用户可以明确要求改变天气或时代，但那是有意的再创作，不是忠实纪录转换。

## Adding a profile / 扩展绘制风格

1. 复制 [Profile 模板](templates/profile-template.md) 到 `profiles/<new-id>.md`，填写线条、色组、明暗、背景、人物/物体、介质、兼容性、保真边界、负面约束和可观察质量检查。
2. 在 `references/cel-era-profiles.md` 增加注册记录和控制基底，声明适用条件、自动优先级、模式建议、氛围兼容和冲突处理。
3. 增加契约与正向/反向图片场景，运行测试。既有五个 Profile 是最低覆盖；schema 检查会跟随注册表验证新增文件。
4. 无需修改核心 `SKILL.md` 或 Prompt 工作流；Agent 只按需读取选中的 Profile。

## Adding a mode / 扩展新模式

1. 复制 `templates/mode-template.md` 到 `modes/<new-mode>.md`，用新题材的具体边线、色彩、阴影、保真/禁止规则替换占位符。
2. 在 `references/scene-modes.md` 增加一条注册记录和邻近模式的分流依据。
3. 在 `tests/scenarios.md` 新增正向与反向场景，运行结构测试。
4. **不要修改** 根目录 `SKILL.md` 来注册新模式，它只按需读取注册表中匹配的文件。

新增氛围时对 `templates/atmosphere-template.md`、`atmospheres/<id>.md`、`references/atmosphere-selection.md` 做类似操作。所有氛围自动触发必须有可见证据。

## 开发与测试

只依赖 Python 3 标准库即可运行结构验证：

```bash
python3 -m unittest discover -s tests -p 'test_*.py' -v
```

详细场景与评估表见 [tests/scenarios.md](tests/scenarios.md)。原始 P01–P06 的历史 **NOT RUN** 状态与 v0.1 拼贴 **FAIL** 记录保留。本次摩托日景和城市夜景已生成并视觉检查，方向获用户认可，风格/保真仍有 **PARTIAL** 项；这是固定方法的实测依据，不是受控五风格对照或全模式图片验收。照片及成品保持私有，不上传到公开仓库。

质量门分别报告 **Fidelity** 与 **Style Authenticity**。保真通过但仍是泛化现代数字插画，不能宣布 mature-ova 转换成功。文件结构测试验证指令契约，不证明模型遵循，也不证明五种风格已经达到预期艺术效果。

## Limitations / 已知限制

- Skill 自身只提供决策和 prompt 结构，**no image output** without a connected image-edit model.
- Prompt 无法保证像素级人物身份精度、局部像素锁定、读清模糊文字、被遮挡人数或生物计数。
- 纯 Prompt 也无法保证特定画风与内容保真同时达到预期；可用模型、参考图接口和逐图视觉复查都会影响结果。
- 成果必须视觉审核；通过文件结构测试不代表图片艺术质量测试已通过。
- 不提供未经同意的新人物、天气、品牌、假地点或虚构文案。
- 参考 80–90 年代成熟赛璐璐动画的通用视觉特性，不复刻具体动画作品角色、画面或其官方元素。
- 原始摄影图片和成品不自动发布到本仓库。

## 设计和计划

- [设计规范](docs/superpowers/specs/2026-10-10-photo-cel-studio-design.md)
- [v0.1 开发计划](docs/superpowers/plans/2026-10-10-photo-cel-studio-v0.1.md)
- [v0.2 设计规范](docs/superpowers/specs/2026-10-10-photo-cel-studio-v0.2-design.md)
- [v0.2 开发计划与验证记录](docs/superpowers/plans/2026-10-10-photo-cel-studio-v0.2.md)
